"""Console script for map_it."""
import argparse
import sys

from .main import map_it


def main():
    """Console script for map_it."""
    parser = argparse.ArgumentParser(
        description="Search an address/location you have copied to your clipboard on \
            an online map provider"
    )
    parser.add_argument(
        "-p",
        "--provider",
        choices=["google_maps", "map_quest", "bing_maps"],
        default="google_maps",
        required=False,
        help="An online map provider",
    )
    parser.add_argument(
        "-b",
        "--browser",
        choices=["chromium", "firefox"],
        default="chromium",
        required=False,
        help="An executable webbrowser",
    )

    args = parser.parse_args()

    map_it(args.provider, args.browser)
    # print("Arguments: " + str(args._))
    # print("Replace this message by putting your code into " "map_it.cli.main")
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
