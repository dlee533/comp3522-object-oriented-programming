"""
(6 Marks)
The code below reads a series of strings from data.txt and saves them into file_names list

It then does the following using a SINGLE-LINE list comprehension:
    1. Determines if the string contains a json or txt extension
    2. Creates a list containing the [file name string and FileType enum] and assigns it to the types_list list
"""

import enum
from enum import auto
from pathlib import Path

class FileType(enum.Enum):
    JSON = auto()
    TXT = auto()


file_names = []  # List to store file names read from data.txt

# TODO - Write code to read data.txt and add the strings to the file_names list
file_path = "data.txt"

with open(file_path, mode="r", encoding="utf-8") as file:
    for line in file:
        file_names.append(line.strip())

# TODO - Replace "???" with a single-line list comprehension that:
# - Determines if the string contains a json or txt extension
# - Create a list containing the [file name string and FileType enum] and assign it to the types_list list
types_list = [[file_name, FileType.JSON] if Path(file_name).suffix == ".json" else [file_name, FileType.TXT] for file_name in file_names]

print(types_list)
# expected output: [['birds.json', <FileType.JSON: 1>], ['cats.txt', <FileType.TXT: 2>], ['dogs.txt', <FileType.TXT: 2>]]
