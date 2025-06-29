"""
A File Processor Program.
Reads a text file and shows the number of lines, words, and characters.
Logs inputs and file reading action.

Methods:
    file_processor: Get a file name and read the file,
        then return the number of characters, newlines, and words.
    main: The main method to gives user inputs and logs the program
        with possible exceptions. Other methods call in it.
"""
from pathlib import Path
import string
import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Set and config file handlers
file_handler = logging.FileHandler("logs/fileprocessor_logs.log")
file_handler.setLevel(logging.WARNING)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Set and config stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(stream_formatter)

# Add handlers to the logger
if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


FILE_NAME = input("Enter the file name to read: ")
ASCII_LETTERS = string.ascii_letters

# Ensure the file exists
Path(FILE_NAME).touch(exist_ok=True)


def file_processor(file_name: str) -> tuple:
    """
    Reads a file content

    Arguments:
        file_name (str): The file will be written.

    Returns:
        line_number (int): The length of the file's newlines.
        word_number (int): The length of the file's words.
        character_number (int): The legth of the file's characters.
    """
    content = None
    line_number = word_number = character_number = 0

    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        logger.info("File has just read successfully.")

    # Get the length of words with split by spaces
    word_number = len(content.split())

    for char in content:
        # Count characters (ascii letters)
        if char in ASCII_LETTERS:
            character_number += 1
        # Count newlines
        elif char == '\n':
            line_number += 1

    return (line_number, word_number, character_number)


def main():
    """
    The main method for run the program and call other methods.
    Gives user input and logs them, also handle the possible exceptions.
    """


print(file_processor(FILE_NAME))
