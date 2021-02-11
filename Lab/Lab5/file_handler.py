# file handler
import json
import enum
from enum import auto
from pathlib import Path


class FileHandler:
    """
    Handles all file related actions.
    """

    @staticmethod
    def load_data(path, file_extension):
        """
        Load data from file.

        :param path: str
        :param file_extension: int
        :precondition: path must be a string
        :precondition: file_extension must be an int(-1, 0, 1)
        :return: dict
        """
        # if file path doesn't exist, raise appropriate error (file not found)
        if file_extension == -1:
            raise InvalidFileTypeError
        elif not Path(path).exists():
            raise FileNotFoundError(f"File ({path}) not found")

        with (open(path, mode="r", encoding="utf-8")) as file:
            if file_extension is FileExtensions.JSON:
                return json.load(file)
            return json.loads(file.read())

    @staticmethod
    def write_lines(path, lines):
        """
        Write a line to file.

        :param path: str
        :param lines: str
        :precondition: path must be a string
        :precondition: lines must be a string
        :return: None
        """
        with (open(path, mode="a", encoding="utf-8")) as file:
            file.write(lines)


class InvalidFileTypeError(Exception):
    """
    Custom Exception class for invalid file type
    """
    def __init__(self):
        super().__init__(f"Invalid file format entered. Only JSON and TXT files are valid.")


class FileExtensions(enum.Enum):
    """
    Enum for File Extensions
    """
    TXT = auto()
    JSON = auto()
