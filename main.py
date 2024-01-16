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


def get_directory_list(url, top_n_dirs=10, file_format=None):
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
        if file_format is None:
            dir_list = [
                link.get("href")
                for link in links
                if link.get("href").strip().endswith("/")
            ]
            return dir_list[-top_n_dirs:]
        else:
            # Extract File links
            file_list = [
                link.get("href")
                for link in links
                if link.get("href").strip().endswith(file_format)
            ]
            return file_list
    except Exception as e:
        logging.error(f"Error: {traceback.print_exc()}")
        return None


def main():
    # how many months of data to download
    top_n_dir = 1
    url = "https://dumps.wikimedia.org/other/clickstream/"

    dir_list = get_directory_list(url, top_n_dir)
    print("top_n directories", dir_list)
    for dir in dir_list:
        file_list = get_directory_list(url + dir, file_format=".gz")
        print("file_list", file_list)


if __name__ == "__main__":
    # executes only if run as a script
    try:
        main()
    except KeyboardInterrupt:
        print("\n-- KeyboardInterrupt --")
