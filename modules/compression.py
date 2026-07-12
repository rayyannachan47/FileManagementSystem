from core.logger import *
from core.helpers import get_file_path, get_directory_path

import os,shutil,zipfile

def compress_file():
    logger = get_logger("compress_file")
    source = get_file_path("\nEnter file/folder path to compress: ")
    if not os.path.exists(source):
        print("Path does not exist.")
        logger.error(f"Compression Failed | {source}")
        return
    destination = get_directory_path("\nEnter destination directory: ")
    zip_name = input("\nEnter zip file name: ").strip()
    zip_path = os.path.join(destination, zip_name)
    try:
        shutil.make_archive(zip_path, "zip", root_dir=os.path.dirname(source), base_dir=os.path.basename(source))
        print("\nCompression completed successfully.")
        logger.info(f"Compressed | {source} -> {zip_path}.zip")
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nCompression failed.")
        
def decompress_file():
    logger = get_logger("decompress_file")
    try:
        while(True):
            filename=input("\nPlease choose your file : ")
            if(os.path.exists(filename)):
                break
            else:
                print("Sorry!! file doesn't exists")
                logger.error(f"File doesn't exists | {filename}")
        while(True):
            directory=input("\nEnter directory to unzip: ")
            if(os.path.exists(directory)):
                filezip=zipfile.ZipFile(filename)
                filezip.extractall(directory)
                filezip.close() 
                print("\nFiles decompress successfully")
                logger.info(f"Files decompress successfully | {filename}")
                break
            else:                
                logger.error(f"Directory doesn't exists | {directory}")
    except(FileNotFoundError,OSError) as e:
        print("Sorry!! it doesn't exists.")  
        logger.error(f"File doesn't exists | {str(e)}")
