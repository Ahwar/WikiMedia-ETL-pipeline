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
