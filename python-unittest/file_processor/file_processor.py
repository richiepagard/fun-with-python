"""
A File Processor Program.
Reads a text file and shows the number of lines, words, and characters.
"""
from pathlib import Path
import string

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

    with open(file_name, 'r') as file:
        content = file.read()

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
