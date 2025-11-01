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


ASCII_LETTERS = string.ascii_letters


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

    with open(file_name, 'rb') as file:
        # Read and decode the opened file
        content = file.read().decode()
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
    logger.debug("Program started.")

    file_name = ""

    try:
        file_name = input("Enter the file name to read: ")
        # Ensure the file exists
        Path(file_name).touch(exist_ok=True)

        logger.info("Received user input: File name is %s.", file_name)
        logger.info("-" * 40)

    except EOFError:
        logger.exception("End of file error. No input received.")
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    except Exception as occured_exception:
        logger.exception("An unexpected exception occured: %s", occured_exception)
        logger.warning("-" * 40)
        # Re-raise the occured exception
        raise

    # Logs the file_process method
    logger.info("File Processor result: %s", file_processor(file_name))
    logger.info("-" * 40)


if __name__ == '__main__':
    main()
