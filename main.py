# Installed packages

# built-in imports
import logging
import traceback
import sys

# custom imports
from utils.logger import get_logger
from utils.utils import read_config
from src.extract import download_files

# configure logging
get_logger()


def main():
    ### Extract
    # how many months of data to download
    program_config = read_config("PROGRAM")
    # read main program arguments from the config file
    try:
        top_n_dir = int(program_config["no_of_latest_months"])
        url = program_config["main_url"]
        download_dir = program_config["download_directory"]
    except KeyError as e:
        logging.info(f"config {e} not found in the config file")
        sys.exit(1)

    download_files(url, top_n_dir, download_dir)


if __name__ == "__main__":
    # executes only if run as a script
    try:
        main()
        logging.info("Program executed successfully")
    except KeyboardInterrupt:
        print("\n-- KeyboardInterrupt --")
    except Exception as e:
        logging.error(f"Error: {traceback.print_exc()}")
