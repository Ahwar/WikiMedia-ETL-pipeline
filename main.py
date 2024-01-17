# built-in imports
import logging
import traceback
import os

# custom imports
from utils.logger import get_logger
from utils.utils import create_directory, delete_directory, unzip_gz_file
from utils.utils import read_program_arguments, read_db_config
from utils.db import PostGreSQL
from src.extract import get_directory_list, download_file
from src.transformation import transform_file


# configure logging
get_logger()


def main():

    # read program arguments from config file
    logging.info("Reading configuration from config file")
    top_n_dir, url, download_dir = read_program_arguments("PROGRAM")
    db_config = read_db_config("DATABASE")
    logging.info("Configuration read successfully")

    # connect to PostGreSQL database
    logging.info("Connecting to PostGreSQL database")
    db = PostGreSQL()
    db.connect(db_config)
    logging.info("Connected to PostGreSQL database successfully")

    # create table if not exists
    db.create_table_if_not_exists("wiki")

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
        if dir.strip().removesuffix("/") not in db.get_distinct_list("month", "wiki"):
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
                ##########
                ### Transform
                ##########
                logging.info("Transforming file '{}'".format(file))
                df = transform_file(
                    os.path.join(download_dir, dir, lang),
                    file.removesuffix(".gz"),
                    lang,
                    dir.removesuffix("/"),
                )

                logging.info("Transformed file '{}' successfully".format(file))

                ##########
                ### Load
                ##########
                # insert DataFrame data into table
                db.insert(df, table_name="wiki")
        else:
            logging.debug(
                "Monthly data of '{}' already exists in the database, so not inserting that data".format(
                    dir.removesuffix("/")
                )
            )
    db.close()


if __name__ == "__main__":
    # executes only if run as a script
    try:
        main()
        logging.info("Program executed successfully")
    except KeyboardInterrupt:
        print("\n-- KeyboardInterrupt --")
    except Exception as e:
        logging.error(f"Error: {traceback.print_exc()}")
