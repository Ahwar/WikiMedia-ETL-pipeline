# built-in imports
import logging
import traceback
import sys, os

# custom imports
from utils.logger import get_logger
from utils.utils import read_config
from utils.utils import create_directory, delete_directory, unzip_gz_file
from src.extract import get_directory_list, download_file

# configure logging
get_logger()


def read_program_arguments():
    ## Read program arguments from config file
    # how many months of data to download
    program_config = read_config("PROGRAM")
    # read main program arguments from the config file
    try:
        top_n_dir = int(program_config["no_of_latest_months"])
        url = program_config["main_url"]
        download_dir = program_config["download_directory"]
        return top_n_dir, url, download_dir
    except KeyError as e:
        logging.info(f"config {e} not found in the config file")
        sys.exit(1)


def main():

    top_n_dir, url, download_dir = read_program_arguments()
    #########
    ### Extract
    ##########

    # Create download directory if it doesn't exist
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
        delete_directory(os.path.join(download_dir, dir))
        logging.info(
            "Fetching list of files from the directory '{}' at url '{}'".format(
                dir, url + dir
            )
        )
        # get list of files from the directory
        file_list = get_directory_list(url + dir, file_format=".gz")
        logging.info("Fetched files list successfully")
        print("list of files from date {} is {}".format(dir, file_list))
        logging.info("Processing each file '{}'".format(dir))

        ## Loop through files in each directory
        for file in file_list:
            lang = file.split("-")[1].removesuffix("wiki")
            download_file(file, download_dir, url, dir)
            unzip_gz_file(os.path.join(download_dir, dir, lang), file)


if __name__ == "__main__":
    # executes only if run as a script
    try:
        main()
        logging.info("Program executed successfully")
    except KeyboardInterrupt:
        print("\n-- KeyboardInterrupt --")
    except Exception as e:
        logging.error(f"Error: {traceback.print_exc()}")
