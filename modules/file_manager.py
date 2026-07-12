from core.validator import file_exists
from core.logger import *
from core.helpers import *

import os,shutil

def create_file():
    logger = get_logger("create_file")
    filename = input("\nEnter file name: ").strip()
    directory = get_directory_path("\nEnter directory path: ")
    file_path = os.path.join(directory, filename)
    if file_exists(file_path):
        print("File already exists.")
        logger.error(f"File already exists | {file_path}")
        return
    stop_word = "exit"
    try:
        print(f"\nEnter file content ({stop_word} to stop):")
        with open(file_path, "w") as file:
            while True:
                line = input()
                if line == stop_word:
                    break
                file.write(line + "\n")
        print("\nFile created successfully.")
        logger.info(f"Created File | {file_path}")

    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("Unable to create file.")
        
def move_file():
    logger = get_logger("move_file")
    files = get_multiple_files()
    if not files:
        print("No files selected.")
        return
    destination = get_directory_path("\nEnter destination directory: ")
    for file_path in files:
        if not file_exists(file_path):
            print(f"{file_path} does not exist.")
            logger.error(f"Move Failed | {file_path}")
            continue
        try:
            shutil.move(file_path, destination)
            logger.info(f"Moved | {file_path} -> {destination}")
        except Exception as e:
            logger.error(f"Something went wrong | {str(e)}")
            print(f"Unable to move {file_path}")
    print("\nOperation completed.")

def rename_file():
    logger = get_logger("rename_file")
    old_path = get_file_path("\nEnter file path: ")
    if not file_exists(old_path):
        print("File does not exist.")
        logger.error(f"File does not exist | {old_path}")
        return
    new_path = input("Enter new file name/path: ").strip()
    try:
        os.rename(old_path, new_path)
        print("File renamed successfully.")
        logger.info(f"Renamed File | {old_path} -> {new_path}")
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("Rename failed.")
        
def delete_file():
    logger = get_logger("delete_file")
    file_path = get_file_path("\nEnter file path: ")
    if not file_exists(file_path):
        print("File does not exist.")
        logger.error(f"File does not exist | {file_path}")
        return
    try:
        os.remove(file_path)
        print("File deleted successfully.")
        logger.info(f"Deleted File | {file_path}")

    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("Unable to delete file.")    

def copy_file():
    logger = get_logger("copy_file")
    files = get_multiple_files()
    if not files:
        print("No files selected.")
        logger.error(f"No files selected |")
        return
    destination = get_directory_path("\nEnter destination directory: ")
    for file_path in files:
        if not file_exists(file_path):
            print(f"{file_path} does not exist.")
            logger.error(f"Copy Failed | {file_path}")
            continue
        try:
            shutil.copy2(file_path, destination)
            logger.info(f"Copied | {file_path} -> {destination}")
        except Exception as e:
            logger.error(f"Something went wrong | {str(e)}")
            print(f"Unable to copy {file_path}")
    print("\nOperation completed.")        
