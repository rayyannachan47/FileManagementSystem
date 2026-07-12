import logging
import os
from datetime import datetime

def get_logger(module_name):
    date = datetime.now().strftime("%d-%m-%Y")
    log_dir = os.path.join("logs", date, module_name.lower())
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{module_name.lower()}.log")
    logger = logging.getLogger(module_name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            "%d-%m-%Y %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger