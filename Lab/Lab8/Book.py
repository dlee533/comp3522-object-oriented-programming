from Lab8.Item import Item


class Book(Item):
    """
    Represents a single book in a catalogue which is identified through its call number.
    """

    def __init__(self,  author: str, **kwargs):
        """
        Initializes a Book.

        :param author: a string
        :param **kwargs: key value pairs for Item class
        """
        super().__init__(**kwargs)
        self._author = author

    def __str__(self) -> str:
        """
        Return string description of object.

        :return: string
        """
        return f"Book: {self._title}\n" \
               f"Call Number: {self._call_num}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}"
