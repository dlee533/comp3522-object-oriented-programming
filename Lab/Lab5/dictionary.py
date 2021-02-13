# dictionary.py
import difflib
from pathlib import Path

from Lab.Lab5.file_handler import InvalidFileTypeError, FileHandler, FileExtensions


class Dictionary:
    """Dictionary class that represents dictionary."""
    END_COMMAND = "exitprogram"
    QUERY_HISTORY_FILEPATH = "query_history.txt"

    def __init__(self):
        """
        Initializes the instance variables.
        """
        self._dictionary = None
        self._loaded = False

    def load_dictionary(self, filepath):
        """
        Loads the words and definitions in file.

        :param filepath: str
        :precondition: filepath must be a string
        :return: Boolean
        """
        if Path(filepath).suffix == ".txt":
            extension = FileExtensions.TXT
        elif Path(filepath).suffix == ".json":
            extension = FileExtensions.JSON
        else:
            extension = -1

        try:
            self._dictionary = FileHandler.load_data(filepath, extension)
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e.args[0]}")
            return False
        except InvalidFileTypeError as e:
            print(f"InvalidFileTypeError: {e.args[0]}")
            return False
        except Exception as e:
            print(f"Error: {e.args[0]}")
            return False
        else:
            self._loaded = True
            return True

    def query_definition(self, word):
        """
        Query definition.

        :param word: str
        :precondition: word must be a string
        :return: str
        """
        if not self._loaded:
            print("Dictionary not loaded")
            return

        if word not in self._dictionary:
            list_dictionary_words = list(self._dictionary)
            similar_results = difflib.get_close_matches(word, list_dictionary_words, cutoff=0.5)
            if len(similar_results) == 0:
                print("Your entered word was not found.")
                return
            print("We could not find the word you entered, but found the following similar results:")
            print(*(result for result in similar_results), sep=", ")
            print()
            return None

        definitions = self._dictionary[word]
        formatted_definition = ""
        num = 1
        for definition in definitions:
            formatted_definition += str(num) + ". " + definition + "\n"
            num += 1
        FileHandler.write_lines(Dictionary.QUERY_HISTORY_FILEPATH, f"{word}:\n{formatted_definition}\n")
        return formatted_definition

    def simulate_dictionary(self):
        """
        Simulates the dictionary program.

        :return: None
        """
        file_path = input("Please enter the path to your dictionary file (e.g. data.json): ").lower().strip()

        self.load_dictionary(file_path)
        if not self._loaded:
            return

        user_query = input("Please enter a word (or enter 'exitprogram' to exit the program): ").lower().strip()
        while user_query != "exitprogram":
            definition = self.query_definition(user_query)
            if definition is not None:
                print("Definition(s) for the word " + user_query + ":\n" + definition)
            user_query = input("Please enter a word (or enter 'exitprogram' to exit the program): ").lower().strip()

def main():
    """
    Creates a Dictionary object and runs the dictionary program simulation.
    """
    dictionary = Dictionary()
    dictionary.simulate_dictionary()

    print("Thanks for using this program!")


if __name__ == "__main__":
    main()
