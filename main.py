# Installed packages
import requests
from bs4 import BeautifulSoup

# built-in imports
import logging
from datetime import datetime
import traceback
import sys

# custom imports
from utils.logger import get_logger
from utils.api import make_http_get_request

# configure logging
get_logger()


def get_directory_list(url, top_n=10):
    try:
        # Send an HTTP request to the webpage
        response = make_http_get_request(url)
        if response is None:
            logging.error(
                f"Error Occured while fetching the URL: {url}, exiting the program..."
            )
            sys.exit(1)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all links in the HTML content
        links = soup.find_all("a")

        # Extract top most directory links
        dir_list = [
            link.get("href") for link in links if link.get("href").strip().endswith("/")
        ]
        return dir_list[-top_n:]
    except Exception as e:
        logging.error(f"Error: {traceback.print_exc()}")
        return None


def main():
    dir_list = get_directory_list(
        "https://dumps.wikimedia.org/other/clickstream/", top_n=1
    )
    print("top_n directories", dir_list)


if __name__ == "__main__":
    # executes only if run as a script
    try:
        main()
    except KeyboardInterrupt:
        print("\n-- KeyboardInterrupt --")
