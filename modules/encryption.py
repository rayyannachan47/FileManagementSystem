from cryptography.fernet import Fernet, InvalidToken

from core.key_manager import load_key
from core.helpers import get_file_path
from core.validator import file_exists
from core.logger import *

def encrypt_file():
    logger = get_logger("encrypt_file")
    file_path = get_file_path("\nEnter file path: ")
    if not file_exists(file_path):
        print("File does not exist.")
        logger.error(f"File does not exist | {file_path}")
        return
    try:
        key = load_key()
        cipher = Fernet(key)
        with open(file_path, "rb") as file:
            data = file.read()
        encrypted = cipher.encrypt(data)
        with open(file_path, "wb") as file:
            file.write(encrypted)
        print("\nFile encrypted successfully.")
        logger.info(f"Encrypted | {file_path}")
    except Exception as e:
        logger.error(f"Something went wrong | {str(e)}")
        print("\nEncryption failed.")
        
def decrypt_file():
    logger = get_logger("decrypt_file")
    file_path = get_file_path("\nEnter file path: ")
    if not file_exists(file_path):
        print("File does not exist.")
        logger.error(f"File does not exist | {file_path}")
        return
    try:
        key = load_key()
        cipher = Fernet(key)
        with open(file_path, "rb") as file:
            encrypted = file.read()
        decrypted = cipher.decrypt(encrypted)
        with open(file_path, "wb") as file:
            file.write(decrypted)
        print("\nFile decrypted successfully.")
        logger.info(f"Decrypted | {file_path}")
    except InvalidToken:
        print("\nInvalid encryption key or corrupted file.")
        logger.error(f"Invalid Token | {file_path}")
    except Exception as e:
        print("\nDecryption failed.")
        logger.error(f"Something went wrong | {str(e)}")
