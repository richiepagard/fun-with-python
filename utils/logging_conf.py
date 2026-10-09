import os
import logging
from logging import getLogger

from colorama import Fore, Style, init


init(autoreset=True)


# Logs configuration
os.makedirs('logs', exist_ok=True)


def base_logger(logger: getLogger):
    # Set custom level for logger
    logger.setLevel(logging.DEBUG)

    # Declare handlers
    file_handler = logging.FileHandler('logs/fwp.log')
    stream_handler = logging.StreamHandler()

    # Determine and set specific formatter for file handler
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    # Determine and set specific formatter for stream handler
    stream_formatter = logging.Formatter(
        f'{Fore.MAGENTA}%(asctime)s{Style.RESET_ALL} - {Fore.BLUE}%(name)s{Style.RESET_ALL} - %(message)s'
    )
    stream_handler.setFormatter(stream_formatter)

    # Set specific level for handlers
    file_handler.setLevel(logging.WARNING)
    stream_handler.setLevel(logging.DEBUG)

    # Checks if the logger does not have any handlers, then add the handlers to the logger
    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
