import os
import shutil
import logging

def create_directory(directory):
    logging.info("Creating directory '{}'".format(directory))
    if not os.path.exists(directory):
        os.makedirs(directory)


def delete_directory(dir):
    # Remove directory and its contents recursively
    logging.info("Deleting directory '{}'".format(dir))
    if os.path.exists(dir):
        shutil.rmtree(dir)
