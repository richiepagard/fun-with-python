"""
A File Processor Program.
Reads a text file and shows the number of lines, words, and characters.
"""
from pathlib import Path

FILE_NAME = input("Enter the file name to read: ")

# Ensure the file exists
Path(FILE_NAME).touch(exist_ok=True)


def file_processor(file_name: str) -> str:
    content = None

    with open(file_name, 'r') as file:
        content = file.read()

    return content


print(file_processor(FILE_NAME))
