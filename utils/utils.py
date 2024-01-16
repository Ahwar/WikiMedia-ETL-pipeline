import os
import shutil


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def delete_directory(download_dir, dir):
    # Remove directory and its contents recursively
    if not os.path.exists(download_dir):
        shutil.rmtree(os.path.join(download_dir, dir))
