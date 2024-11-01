import concurrent
import html2text
import json
import logging
import openai
import re
import requests
import sys
import warnings

from bs4 import BeautifulSoup

from typing import Optional, Union, List
from contextlib import contextmanager

html2text_markdown_converter = html2text.HTML2Text()
html2text_markdown_converter.wrap_links = False
html2text_markdown_converter.ignore_links = False
html2text_markdown_converter.body_width = 0  # Disable line wrapping

SYSTEMPROMPT = "I have scraped a webpage, and converted it from HTML into Markdown format. I'd like you to answer some questions about it."
PROMPT_HUMAN_READABLE_CHECK = "Does this look like human-readable content? Please respond with one word: Yes or No."
INVPROMPT_NOT_EVERY_LINE_RELEVANT = """
No, not every line is relevant to the page's purpose or topic. The page contains various elements, including:

1. **Navigation Links**: Lines that provide links to other sections of the website. These are not directly related to the specific content of the page.

2. **Images and Icons**: Lines that include images, such as social media icons. While they contribute to the overall design and branding of the page, they do not pertain to its specific topic.

3. **Footnotes and References**: Lines that contain footnotes and references. While they provide context and support for the information presented, they may not be essential for understanding the main content.

4. **Feedback and Contact Information**: Lines that invite user feedback or provide contact information. These are useful for user interaction but are not directly related to the content.

5. **Copyright, Cookie Policy Notices, FOIA Notices, etc.**: Lines that provide standard legal notifications for users. They are typically "boilerplate", and do not relate to the page's content.

6. **Login and User Management**: Lines that allow a user to sign into the website. This can provide a personalized user experience, but is not directly relevant to the page's content.

7. **Page Version History**: Lines that discuss the page's version history generally aren't relevant to the page's content.

8. **Advertisement**: Lines that contain advertisements aren't relevant to the page's content.

And so on.

Overall, while many lines contribute to the page's functionality and user experience, not all are directly relevant to the page's specific topic.
"""
PROMPT_BATCH_LINE_FILTER = """
Examining specifically these lines, let's filter out lines that aren't relevant to the page's topic or purpose, leaving only those that are relevant.

Go through each numbered line of this excerpt. For each numbered line, briefly discuss whether or not the line is relevant to the page's contents or whether it's one of the irrelevant line types you've mentioned above (or some other irrelevant line type). Follow this description with a dash, and then give it a designation of either "relevant" or "irrelevant".

Here's an example of what your response should look like:
1. Header logo, an image or icon - irrelevant
2. Title of the page - relevant
3. Menu link, a navigation link - irrelevant
4. Login link - irrelevant
5. Sitemap link, part of the navigation system - irrelevant
6. Body text - relevant
7. Body text - relevant
8. Advertisement - irrelevant
9. Contact Us link - irrelevant
10. Revision History header, part of a page version history section - irrelevant
etc.

Make sure that the line numbers of your output match the line numbers of the excerpt.
"""


LOGGER = logging.getLogger("webpage2content")


# With the help of this function, we can prevent urllib3 from spewing obnoxious
# warnings about SSL certificates and other HTTP-related stuff while fetching URLs.
@contextmanager
def suppress_warnings():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        yield


# Fix a ridiculous formatting error in which sometimes links get double slashes.
def _remove_double_slashes(url: str):
    m = re.match(r"^(\w+)\:(/*)(.*)", url)
    if not m:
        # Doesn't start with a protocol designator. Doesn't look like a URL.
        return url

    protocol = m.group(1)

    s = m.group(3)
    s = re.sub(r"/+", "/", s)

    retval = f"{protocol}://{s}"
    return retval


def _get_page_as_markdown(url: str) -> str:
    if not url:
        return
    url = f"{url}"
    url = _remove_double_slashes(url)

    response = None

    try:
        # Get the site's presumed base URL from the URL itself.
        url_proto, url_therest = url.split("//")
        url_domain = url_therest.split("/")[0]
        base_url = f"{url_proto}//{url_domain}"
    except Exception:
        # Log the exception with traceback
        LOGGER.exception(
            f'Exception in _get_page_as_markdown while trying to parse URL (string is not a valid URL): "{url}"'
        )
        return None

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.126 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }

        with suppress_warnings():
            response = requests.get(
                url,
                timeout=60,
                verify=False,
                headers=headers,
            )
    except Exception:
        # Log the exception with traceback
        LOGGER.exception("Exception in _get_page_as_markdown while fetching page")
        return None

    if not response:
        LOGGER.warning(f"No content retrieved from URL: {url}")
        return None

    if response.status_code != 200:
        LOGGER.warning(f"Fetch failed for URL: {url}")
        return None

    # Look for an HTML tag to confirm that this is in fact HTML content.
    # Look for a <base> tag to get the base URL.
    # If it doesn't exist, just keep the base URL that was gleaned from the target URL.
    try:
        content = response.content.decode("utf-8", errors="ignore")
        soup = BeautifulSoup(content, "html.parser")

        html_tag = soup.find("html")
        if not html_tag:
            LOGGER.warning("_get_page_as_markdown failed because no html tag")
            return None

        base_tag = soup.find("base")
        if base_tag:
            base_url = base_tag["href"]
    except Exception:
        # Log the exception with traceback
        LOGGER.exception("Exception in _get_page_as_markdown while parsing HTML")
        return None

    html_content = response.text
    html2text_markdown_converter.baseurl = base_url

    markdown_content = None
    try:
        markdown_content = html2text_markdown_converter.handle(html_content)
    except Exception:
        # Log the exception with traceback
        LOGGER.exception("Exception in _get_page_as_markdown while converting HTML")
        return None

    if not markdown_content:
        return None

    # We'll now strip lines and consolidate whitespace.
    lines = markdown_content.splitlines()
    lines = [line.strip() for line in lines]
    markdown_content = "\n".join(lines)
    markdown_content = re.sub(r"\n\n\n+", "\n\n", markdown_content)

    return markdown_content


def _call_gpt(
    conversation: Union[str, dict, List[dict]],
    openai_client: openai.OpenAI,
) -> str:
    if isinstance(conversation, str):
        conversation = [{"role": "user", "content": conversation}]
    elif isinstance(conversation, dict):
        conversation = [conversation]

    answer_full = ""
    while True:
        LOGGER.debug(
            f"webpage2content._call_gpt calling chat completion "
            f"with conversation of {len(conversation)} messages. "
            f"Last message is {len(conversation[-1]['content'])} chars long."
        )

        completion = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation,
            temperature=0,
        )

        answer = completion.choices[0].message.content
        answer_full += answer + "\n"

        LOGGER.debug(
            f"webpage2content._call_gpt got answer of length {len(answer)}, "
            f"appending to full answer currently at length {len(answer_full)}"
        )

        conversation.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )
        conversation.append(
            {
                "role": "user",
                "content": "Please continue from where you left off.",
            }
        )

        if completion.choices[0].finish_reason == "length":
            LOGGER.debug(
                "webpage2content._call_gpt finish reason length, continuing loop"
            )
            continue

        break

    answer_full = answer_full.strip()
    return answer_full


def webpage2content(url: str, openai_client: openai.OpenAI):
    if type(url) != str:
        LOGGER.warning("webpage2content got a URL that isn't a string.")
        return None

    url = url.strip()
    if not url:
        LOGGER.warning("webpage2content got empty URL.")
        return None

    markdown = _get_page_as_markdown(url)
    if not markdown:
        return None

    if not isinstance(markdown, str):
        LOGGER.error("markdown somehow came back as something other than a string.")
        return None

    markdown = markdown.strip()
    if not markdown:
        return None

    # TODO: Break up the markdown into pieces if the webpage is too big.

    try:
        conversation = [
            {"role": "system", "content": SYSTEMPROMPT},
            {"role": "user", "content": markdown},
            {"role": "user", "content": PROMPT_HUMAN_READABLE_CHECK},
        ]
        gptreply_is_human_readable = _call_gpt(
            conversation=conversation,
            openai_client=openai_client,
        )
        is_human_readable = "yes" in gptreply_is_human_readable.lower()
        if not is_human_readable:
            LOGGER.warning(f"Page at URL {url} is not human-readable")
            return None

    except Exception:
        LOGGER.exception("Exception in webpage2content checking human readability")
        return None

    description = ""
    try:
        conversation = [
            {"role": "system", "content": SYSTEMPROMPT},
            {"role": "user", "content": markdown},
            {
                "role": "user",
                "content": "What is the purpose or topic of this page? Describe it in your own words.",
            },
        ]
        description = _call_gpt(
            conversation=conversation,
            openai_client=openai_client,
        )

    except Exception:
        LOGGER.exception("Exception in webpage2content getting page description")
        return None

    mdlines = [""]
    for line in markdown.splitlines():
        line = line.strip()
        if not line:
            # It's a blank line, which groups with the previous line.
            mdlines[len(mdlines) - 1] += "\n"
        else:
            mdlines.append(line)

    if not mdlines[0].strip():
        # The first line is blank.
        mdlines = mdlines[1:]

    # In case we need the original unmodified lines...
    # mdlines_orig = json.loads(json.dumps(mdlines))

    markdown_with_linenums = "\n".join(
        [f"{i+1}. {line}" for i, line in enumerate(mdlines)]
    )

    main_conversation = [
        {
            "role": "system",
            "content": f"{SYSTEMPROMPT} I've numbered the lines.",
        },
        {"role": "user", "content": markdown_with_linenums},
        {"role": "user", "content": "Describe this page."},
        {"role": "assistant", "content": description},
        {
            "role": "user",
            "content": "Is every line relevant to this page's purpose or topic?",
        },
        {"role": "assistant", "content": INVPROMPT_NOT_EVERY_LINE_RELEVANT},
    ]

    LINE_BATCH_SIZE = 20

    def _fn_filter_batch_lines(iline: int):
        LOGGER.debug(
            f"Processing line batch {iline+1} through {iline+LINE_BATCH_SIZE} of {len(mdlines)} on {url}"
        )
        batchlines = mdlines[iline : iline + 20]
        mdbatch = "\n".join(
            [f"{iline+i+1}. {line}" for i, line in enumerate(batchlines)]
        )

        conversation = json.loads(json.dumps(main_conversation))
        conversation.extend(
            [
                {
                    "role": "user",
                    "content": (
                        f"Let's specifically consider lines {iline+1} through {iline+LINE_BATCH_SIZE}.\n"
                        f"\n"
                        f"{mdbatch}"
                    ),
                },
                {"role": "user", "content": PROMPT_BATCH_LINE_FILTER},
            ]
        )
        try:
            gptreply_batch_filtration = _call_gpt(
                conversation=conversation,
                openai_client=openai_client,
            )
        except Exception:
            LOGGER.exception(
                f"Error during GPT call on {url} during batch for lines {iline+1} through {iline+LINE_BATCH_SIZE}"
            )

        gptreplylines = gptreply_batch_filtration.splitlines()
        for gptreplyline in gptreplylines:
            if "." not in gptreplyline:
                continue
            linenumstr, linetext = gptreplyline.split(".", maxsplit=1)
            try:
                linenum = int(linenumstr)
            except ValueError:
                # Not a number
                continue
            linenum = linenum - 1
            linetext = linetext.strip().lower()
            if linetext.endswith("irrelevant"):
                mdlines[linenum] = ""

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(_fn_filter_batch_lines, iline)
            for iline in range(0, len(mdlines), LINE_BATCH_SIZE)
        ]

        # Wait for all concurrences to finish.
        for future in concurrent.futures.as_completed(futures):
            try:
                LOGGER.info(
                    f"Concurrent thread finished with result: {future.result()}"
                )
            except Exception:
                LOGGER.exception("Concurrent thread threw an exception.")

    mdfiltered = "\n".join([l for l in mdlines if l])

    LOGGER.debug(f"webpage2content has constructed filtered markdown for {url}")
    return mdfiltered


def main():
    import argparse
    import dotenv
    import os

    # Read the version from the VERSION file
    with open(os.path.join(os.path.dirname(__file__), "VERSION"), "r") as version_file:
        version = version_file.read().strip()

    parser = argparse.ArgumentParser(
        description=(
            "A simple Python package that takes a web page (by URL) and extracts its "
            "main human-readable content. It uses LLM technology to remove all of the "
            "boilerplate webpage cruft (headers, footers, copyright and accessibility "
            "notices, advertisements, login and search controls, etc.) that isn't part "
            "of the main content of the page."
        )
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {version}",
        help="Show the version number and exit.",
    )

    parser.add_argument(
        "-l",
        "--log-level",
        help="Sets the logging level. (default: %(default)s)",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )

    parser.add_argument(
        "-u",
        "--url",
        help="The URL to read.",
        type=str,
    )
    parser.add_argument(
        "url_arg",
        help="Same as --url, but specified positionally.",
        type=str,
        nargs="?",
    )

    parser.add_argument(
        "-k",
        "--key",
        help="OpenAI API key. If not specified, reads from the environment variable OPENAI_API_KEY.",
        type=str,
        default="",
    )
    parser.add_argument(
        "key_arg",
        help="Same as --key, but specified positionally.",
        type=str,
        nargs="?",
    )

    parser.add_argument(
        "-o",
        "--org",
        help="OpenAI organization ID. If not specified, reads from the environment variable OPENAI_ORGANIZATION. "
        "If no such variable exists, then organization is not used when calling the OpenAI API.",
        type=str,
        default="",
    )
    parser.add_argument(
        "org_arg",
        help="Same as --org, but specified positionally.",
        type=str,
        nargs="?",
    )

    args = parser.parse_args()

    if args.log_level:
        log_level = logging.getLevelName(args.log_level)
        LOGGER.setLevel(log_level)

    dotenv.load_dotenv()

    openai_api_key = args.key or args.key_arg or os.getenv("OPENAI_API_KEY")
    openai_org_id = args.org or args.org_arg or os.getenv("OPENAI_ORGANIZATION_ID")
    url = args.url or args.url_arg

    if not url:
        parser.error("URL is required.")
    if not openai_api_key:
        parser.error("OpenAI API key is required.")

    openai_client = openai.OpenAI(api_key=openai_api_key, organization=openai_org_id)

    s = webpage2content(
        url=url,
        openai_client=openai_client,
    )
    print(s)


if __name__ == "__main__":
    main()
