from core.logger import *
import os, string
def get_drives():
    drives = []
    for drive in string.ascii_uppercase:
        if os.path.exists(f"{drive}:\\"):
            drives.append(f"{drive}:\\")
    return drives


def search_file():
    logger = get_logger("search_file")
    filename = input("\nEnter file name: ").strip()
    drives = get_drives()
    for drive in drives:
        print(f"\nSearching in {drive} ...")
        for root, dirs, files in os.walk(drive):
            for file in files:
                if file.lower().endswith(filename.lower()):
                    print(os.path.join(root, file))
                    logger.info(f"Search File | {os.path.join(root, file)}")

    print("\nSearch Completed.")