# Installed packages
import requests
from bs4 import BeautifulSoup

# built-in imports
import logging
from datetime import datetime
import traceback
import sys, os
import shutil

# custom imports
from utils.logger import get_logger
from utils.api import make_http_get_request
from utils.utils import create_directory, delete_directory

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


def download_file(file_name, download_dir, url, dir):

    logging.info(
        "Downloading file '{}' from the directory '{}' at url '{}'".format(
            file_name, dir, url + dir + file_name
        )
    )
    # create directory if not exists
    lang = file_name.split("-")[1].removesuffix("wiki")
    combined_path = os.path.join(download_dir, dir, lang)
    create_directory(combined_path)

    # Download the file
    response = make_http_get_request(url + dir + file_name)
    if response is None:
        logging.error(
            f"Error Occured while downloading file from URL: {url}, exiting the program..."
        )
        sys.exit(1)
    logging.info(f"Downloaded file successfully: {file_name}")
    print("file downloaded", file_name)

    # Save the file
    logging.info("Saving the file '{}'".format(file_name))
    file_path = os.path.join(combined_path, file_name)
    with open(file_path, "wb") as f:
        f.write(response.content)
    logging.info(f"Saved the file successfully at {file_path}")


def main():
    ### Extract
    # how many months of data to download
    top_n_dir = 1
    url = "https://dumps.wikimedia.org/other/clickstream/"

    # Create directory named 'download' if it doesn't exist
    download_dir = "downloads"
    create_directory(download_dir)

    # Fetch list of directories
    logging.info(
        "Fetching list of top '{}' Directories from the '{}'".format(top_n_dir, url)
    )
    dir_list = get_directory_list(url, top_n_dir)
    logging.info("Fetched directories list successfully")
    print("top_n directories", dir_list)

    # Fetch list of files from the directories

    logging.info("Fetching list of .gz files from the directories")
    for dir in dir_list:
        delete_directory(download_dir, dir)
        logging.info(
            "Fetching list of files from the directory '{}' at url '{}'".format(
                dir, url + dir
            )
        )
        file_list = get_directory_list(url + dir, file_format=".gz")
        logging.info("Fetched files list successfully")
        print("list of files from date {} is {}".format(dir, file_list))

        for file in file_list:
            download_file(file, download_dir, url, dir)


if __name__ == "__main__":
    # executes only if run as a script
    try:
        main()
    except KeyboardInterrupt:
        print("\n-- KeyboardInterrupt --")
    except Exception as e:
        logging.error(f"Error: {traceback.print_exc()}")
