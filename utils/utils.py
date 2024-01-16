import os
import shutil
import logging
from configparser import ConfigParser

def create_directory(directory):
    logging.info("Creating directory '{}'".format(directory))
    if not os.path.exists(directory):
        os.makedirs(directory)


def delete_directory(dir):
    # Remove directory and its contents recursively
    logging.info("Deleting directory '{}'".format(dir))
    if os.path.exists(dir):
        shutil.rmtree(dir)


def read_config(section, filename='config.ini'):
    parser = ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        # read section
        section_ = parser[section]
        try:
            config = {key: section_[key] for key in section_}
            return config
        except KeyError as e:
            logging.info(f'config {e} not found in the {filename} config file under section: {section}')
            # sys.exit(1)
    else:
        raise Exception(f'Section {section} not found in the {filename} file')


