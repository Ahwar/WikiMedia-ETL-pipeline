import os
import shutil
import logging
from configparser import ConfigParser
import gzip
import sys


def create_directory(directory):
    logging.info("Creating directory '{}'".format(directory))
    if not os.path.exists(directory):
        os.makedirs(directory)


def delete_directory(dir):
    # Remove directory and its contents recursively
    logging.info("Deleting directory '{}'".format(dir))
    if os.path.exists(dir):
        shutil.rmtree(dir)


def read_config(section, filename="config.ini"):
    parser = ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        # read section
        section_ = parser[section]
        try:
            config = {key: section_[key] for key in section_}
            return config
        except KeyError as e:
            logging.info(
                f"config {e} not found in the {filename} config file under section: {section}"
            )
    else:
        logging.error(f"Section {section} not found in the {filename} config file")
        sys.exit(1)


def unzip_gz_file(gz_file_path, file_name):
    output_file_name = file_name.removesuffix(".gz")
    input_file_path = os.path.join(gz_file_path, file_name)
    logging.info(f"Extracting file {file_name} to {gz_file_path + output_file_name}")
    with gzip.open(input_file_path, "rb") as gz_file:
        with open(os.path.join(gz_file_path, output_file_name), "wb") as output_file:
            shutil.copyfileobj(gz_file, output_file)
    logging.info(f"Extracted file {file_name} successfully")


def read_program_arguments(section, config_file="config.ini"):
    """
    Read program arguments from the config file.

    Args:
        section (str): The section name in the config file.
        config_file (str, optional): The path to the config file. Defaults to "config.ini".

    Returns:
        tuple: A tuple containing the top_n_dir (int), url (str), and download_dir (str).
    """

    ## Read program arguments from config file
    # how many months of data to download
    program_config = read_config(section, config_file)
    # read main program arguments from the config file
    try:
        top_n_dir = int(program_config["no_of_latest_months"])
        url = program_config["main_url"]
        download_dir = program_config["download_directory"]
        return top_n_dir, url, download_dir
    except KeyError as e:
        logging.info(f"config {e} not found in the config file")
        sys.exit(1)


def read_db_config(section, config_file="config.ini"):
    """
    Read database configuration from the specified section in the config file.

    Args:
        section (str): The section name in the config file.
        config_file (str, optional): The path to the config file. Defaults to "config.ini".

    Returns:
        dict: A dictionary containing the database configuration parameters.

    Raises:
        KeyError: If any of the required configuration parameters are missing in the config file.
    """

    ## Read database arguments from config file
    # how many months of data to download
    db_config = read_config(section, config_file)
    config = {}
    # read main program arguments from the config file
    try:
        config["database"] = db_config["database"]
        config["user"] = db_config["user"]
        config["password"] = db_config["password"]
        config["host"] = db_config["host"]
        config["port"] = db_config["port"]
        return config
    except KeyError as e:
        logging.info(
            f"config {e} not found in the config file under section: {section}"
        )
        sys.exit(1)
