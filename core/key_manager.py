from cryptography.fernet import Fernet
import os

KEY_FILE = os.path.join("config", "secret.key")

def generate_key():
    os.makedirs("config", exist_ok=True)
    try:
        with open(KEY_FILE, "rb") as file:
            key = file.read()
        Fernet(key)
    except Exception:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)

def load_key():
    generate_key()
    with open(KEY_FILE, "rb") as file:
        return file.read()