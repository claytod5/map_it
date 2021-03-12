"""map_it.py: Finds an address in the clipboard on an online map provider """

import re
import webbrowser

import pyperclip

# patterns to replace unwanted carriage returns and spaces
pattern1 = re.compile(r"(\n|\r)")
pattern2 = re.compile(r"\s{2,100}")

providers = {
    "google_maps": "https://google.com/maps/search/",
    "map_quest": "https://www.mapquest.com/search/results?query=",
    "bing_maps": "https://www.bing.com/maps?where1=",
}


def format_url(provider):
    """Returns a new url from appropriate provider and with search string.

    Args:
        provider: An online map provider. CLI interface defaults to "google_maps"

    Returns:
        A complete url with provider prefix and search_string suffix

    Example:
        "https://google.com/maps/search/Seattle"

    """
    clipboard_contents = pyperclip.paste()
    clipboard_contents = pattern1.sub("", clipboard_contents)
    clipboard_contents = pattern2.sub("", clipboard_contents)
    return f"{providers[provider]}{clipboard_contents}"


def map_it(provider, browser):
    """Gather clipboard contents, replace non-wanted characters, and open browser url.

    Args:
        provider: An online map provider. CLI interface defaults to "google_maps"
        browser: Name of browser. CLI interface defaults to "chromium"
    """
    browser_controller = webbrowser.get(browser)
    browser_controller.open(format_url(provider))
