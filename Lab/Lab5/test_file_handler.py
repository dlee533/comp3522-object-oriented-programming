from unittest import TestCase
import os

from Lab.Lab5.file_handler import InvalidFileTypeError, FileHandler, FileExtensions


class TestFileHandler(TestCase):
    def test_load_data_invalid_file_type(self):
        """Tests if the method raises InvalidFileTypeError when passed invalid file type"""
        self.assertRaises(InvalidFileTypeError, FileHandler.load_data, "path", -1)

    def test_load_data_file_not_found(self):
        """Tests if the method raises FileNotFoundError when passed invalid file path"""
        self.assertRaises(FileNotFoundError, FileHandler.load_data, "path", FileExtensions.TXT)

    def test_load_data_file_not_found1(self):
        """Tests if the method raises FileNotFoundError when passed invalid file path"""
        self.assertRaises(FileNotFoundError, FileHandler.load_data, "path", FileExtensions.JSON)

    def test_load_data_return_dict(self):
        """Tests if the method return dict"""
        data = FileHandler.load_data("data.json", FileExtensions.JSON)
        self.assertEqual(type(data), dict)

    def test_load_data_return_dict1(self):
        """Tests if the method return dict when passed text file"""
        data = FileHandler.load_data("data.json", FileExtensions.TXT)
        self.assertEqual(type(data), dict)

    def test_write_lines_create_file(self):
        """Tests if the method creates new file when called"""
        filepath = "testfile_file_handler.txt"
        if os.path.exists(filepath):
            os.remove(filepath)
        FileHandler.write_lines(filepath, "hello world!")
        self.assertTrue(os.path.exists(filepath))
        os.remove(filepath)  # for cleanup after testing

    def test_write_lines_one_line(self):
        """Tests if the method correctly writes a line to the file"""
        filepath = "testfile_file_handler.txt"
        if os.path.exists(filepath):
            os.remove(filepath)
        my_str = "hello world!"
        FileHandler.write_lines(filepath, my_str)
        with (open(filepath, mode="r", encoding="utf-8")) as file:
            data = file.read()
        self.assertEqual(data, my_str)
        os.remove(filepath)  # for cleanup after testing

    def test_write_lines_multiline(self):
        """Tests if the method correctly writes multiple lines to the file"""
        filepath = "testfile_file_handler.txt"
        if os.path.exists(filepath):
            os.remove(filepath)
        my_str = "hello world!\nthis is second line\nthis is third line\nfourth line"
        FileHandler.write_lines(filepath, my_str)
        with (open(filepath, mode="r", encoding="utf-8")) as file:
            data = file.read()
        self.assertEqual(data, my_str)
        os.remove(filepath)  # for cleanup after testing

    def test_write_lines_multiline1(self):
        """Tests if the method correctly writes multiple lines to the file"""
        filepath = "testfile_file_handler.txt"
        if os.path.exists(filepath):
            os.remove(filepath)
        my_str = "hello world!\nthis is second line\nthis is third line\nfourth line"
        my_str1 = "\nfifth line\nsixth line"
        FileHandler.write_lines(filepath, my_str)
        FileHandler.write_lines(filepath, my_str1)
        with (open(filepath, mode="r", encoding="utf-8")) as file:
            data = file.read()
        self.assertEqual(data, my_str + my_str1)
        os.remove(filepath)  # for cleanup after testing
