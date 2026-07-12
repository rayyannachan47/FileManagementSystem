from core.helpers import get_directory_path
from core.validator import directory_exists
from core.logger import *
import os
import shutil

def create_directory():
    logger = get_logger("create_directory")
    directory_name = input("\nEnter directory name: ").strip()
    parent_directory = get_directory_path("\nEnter location to create directory: ")
    directory_path = os.path.join(parent_directory, directory_name)
    if directory_exists(directory_path):
        print("\nDirectory already exists.")
        logger.error(f"Directory already exists | {directory_path}")
        return
    try:
        os.mkdir(directory_path)
        print("\nDirectory created successfully.")
        logger.info(f"Directory Created | {directory_path}")
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nUnable to create directory.")

def rename_directory():
    logger = get_logger("rename_directory")
    old_directory = get_directory_path("\nEnter directory path: ")
    new_directory = input("\nEnter new directory name/path: ").strip()
    try:
        os.rename(old_directory, new_directory)
        print("\nDirectory renamed successfully.")
        logger.info(f"Directory Renamed | {old_directory} -> {new_directory}")
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nUnable to rename directory.")

def delete_directory():
    logger = get_logger("delete_directory")
    directory_path = get_directory_path("\nEnter directory path: ")
    try:
        shutil.rmtree(directory_path)
        print("\nDirectory deleted successfully.")
        logger.info(f"Directory Deleted | {directory_path}")
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nUnable to delete directory.")