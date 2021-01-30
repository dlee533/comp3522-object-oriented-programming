import abc
from datetime import datetime


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

    def get_title(self) -> str:
        """
        Returns the title of the book.

        :return: a string
        """
        return self._title.title()

    def get_num_copies(self) -> int:
        """
        Returns the number of copies that are available for this
        specific book.

        :return: an int
        """
        return self._num_copies

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

    @property
    def call_number(self):
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return:
        """
        return self._call_num

    # @call_number.setter
    # def call_number(self, value):
    #     """
    #     This is the decorator way to create a SET property. This would
    #     allow us to invoke this method by simply saying
    #     my_book.call_number = "102.345.992". I've commented this out
    #     since call numbers should not need a setter.
    #     :param value: a string
    #     :precondition value: a unique call number identifier
    #     """
    #     self._call_num = value

    def check_availability(self) -> bool:
        """
        Returns True if the item is available and False otherwise.

        :return: A Boolean
        """
        if self._num_copies > 0:
            return True
        else:
            return False


class Book(Item):
    """
    Represents a single book in a catalogue which is identified through its call number.
    """

    def __init__(self, call_num: str, title: str, num_copies: int, author: str):
        """
        Initializes a Book.

        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies)
        self._author = author

    def __str__(self) -> str:
        """
        Return string description of object.

        :return: string
        """
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}"


class Dvd(Item):
    """
    Represents a single DVD in catalogue which is identified through its call number.
    """

    def __init__(self, call_num: str, title: str, num_copies: int, release_date: datetime, region_code: str):
        """
        Initializes a Dvd.

        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param release_date: a datetime object
        :param region_code: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    def __str__(self) -> str:
        """
        Return string description of object.

        :return: string
        """
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Release Date: {self._release_date}\n" \
               f"Region Code: {self._region_code}"


class Journal(Item):
    """
    Represents a single scientific journal in catalogue which is identified through its call number.
    """

    def __init__(self, call_num: str, title: str, num_copies: int, name: str, issue_number: int, publisher: str):
        """
        Initializes a journal.

        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param name: a string
        :param issue_number: an int
        :param publisher: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        :precondition issue_number: a positive integer
        """
        super().__init__(call_num, title, num_copies)
        self._name = name
        self._issue_number = issue_number
        self._publisher = publisher

    def __str__(self) -> str:
        """
        Return string description of object.

        :return: string
        """
        return f"---- Journal: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}"
