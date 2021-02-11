"""
This module is responsible for unit testing the dictionary.py module.
"""
from unittest import TestCase
from dictionary import Dictionary


class TestDictionary(TestCase):
    """
    Inherits from TestCase and contains the unit tests for dictionary.py
    """


def test_load_dictionary_loaded_true(self):
    """
    Unit test for load_dictionary method in the Dictionary class. Tests if
    the attribute for tracking whether dictionary is loaded or not is equal to True
    when the Dictionary object is loaded with a valid file.
    """
    test_dictionary = Dictionary()
    test_dictionary.load_dictionary("data.json")
    result = test_dictionary._loaded
    self.assertTrue(result)


def test_load_dictionary_loaded_false(self):
    """
    Unit test for load_dictionary method in the Dictionary class. Tests if
    the attribute for tracking whether dictionary is loaded or not is equal to False
    when the Dictionary object is loaded with a invalid file.
    """
    test_dictionary = Dictionary()
    test_dictionary.load_dictionary("invalid_file_path.json")
    result = test_dictionary._loaded
    self.assertFalse(result)


def test_query_definition_valid_query(self):
    """
    Unit test for query_definition method in the Dictionary class. Tests
    whether the formatted definition is returned if a valid query was passed.
    """
    test_dictionary = Dictionary()
    test_dictionary.load_dictionary("data.json")
    result = test_dictionary.query_definition("puppy")
    test_definition = "1. A young dog."
    self.assertEqual(result, f"{test_definition}\n")


def test_query_definition_invalid_query_with_similar_results(self):
    """
    Unit test for query_definition method in the Dictionary class. Tests
    whether None is returned when an invalid query with similar word results in
    the dictionary is passed.
    """
    test_dictionary = Dictionary()
    test_dictionary.load_dictionary("data.json")
    result = test_dictionary.query_definition("puppyyyy")
    self.assertEqual(result, None)


def test_query_definition_invalid_query_with_no_similar_results(self):
    """
    Unit test for query_definition method in the Dictionary class. Tests
    whether None is returned when an invalid query with no similar word results in
    the dictionary is passed.
    """
    test_dictionary = Dictionary()
    test_dictionary.load_dictionary("data.json")
    result = test_dictionary.query_definition("23854297519")
    self.assertEqual(result, None)


def test_query_definition_dictionary_not_loaded(self):
    """
    Unit test for query_definition method in the Dictionary class. Tests
    whether None is returned when trying to query when the dictionary is
    not loaded.
    """
    test_dictionary = Dictionary()
    result = test_dictionary.query_definition("puppy")
    self.assertEqual(result, None)
