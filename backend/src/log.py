import logging
import os

from src.core import settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_logger(log_file_name: str):
    logger = logging.getLogger(log_file_name)
    os.makedirs(settings.LOG_PATH, exist_ok=True)
    handler = logging.FileHandler(f'{settings.LOG_PATH}/{log_file_name}.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
