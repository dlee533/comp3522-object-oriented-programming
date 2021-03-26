import abc


class Item(abc.ABC):
    """
    Represents an item in a library catalogue.
    """

    def __init__(self, call_num: str, title: str, num_copies: int):
        """
        Initializes an Item.

        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies

    @property
    def title(self):
        """
        Property for title.

        :return: title, string
        """
        return self._title

    @property
    def call_num(self):
        """
        Property for call_num.

        :return: call_num, string
        """
        return self._call_num

    def increment_number_of_copies(self):
        """
        Sets the number of copies of an book.

        :return: none
        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        Set's the number of copies of an book.

        :return: none
        """
        self._num_copies -= 1

    def check_availability(self) -> bool:
        """
        Returns True if the item is available and False otherwise.

        :return: A Boolean
        """
        if self._num_copies > 0:
            return True
        else:
            return False
