"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":", "(", "[", "]", ")"]

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read the file
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = "\n".join(book_file.readlines())

        # replace new line characters and common punctuation with replacements
        self.text = self.text.replace("\n", " ")

        for punctuation in self.COMMON_PUNCTUATION:
            self.text = self.text.replace(punctuation, "")

        # convert list of lines to list of words
        self.text = self.text.split()

    def find_unique_words(self):
        """
        Filters out all the words in the text
        :return: a list of all the unique words.
        """
        words_set = set(self.text)
        word_dict = {word.lower(): word for word in words_set}

        return list(word_dict.values())


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    print("\n".join(unique_words))
    print("-" * 50)


if __name__ == '__main__':
    main()
