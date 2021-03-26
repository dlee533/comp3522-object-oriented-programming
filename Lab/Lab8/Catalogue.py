import difflib

from texttable import Texttable

from Lab8.BookFactory import BookFactory
from Lab8.DvdFactory import DvdFactory
from Lab8.Item import Item
from Lab8.ItemType import ItemType
from Lab8.JournalFactory import JournalFactory


class Catalogue:
    """
    The Catalogue consists of a list of items and provides user actions
    related to finding, adding, and removing books from the list.
    """

    def __init__(self, item_list: list):
        """
        Initialize the library with a list of items.

        :param item_list: a sequence of item objects.
        :precondition: item_list must be a list
        """
        self._item_list = item_list

    def _retrieve_item_by_call_num(self, call_num: str) -> Item:
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the library.

        :param call_num: a string
        :precondition: call_num must be a string
        :return: item object if found, None otherwise
        """
        found_item = None
        for library_item in self._item_list:
            if library_item.call_num == call_num:
                found_item = library_item
                break
        return found_item

    def retrieve_item_for_check_out(self, call_num: str) -> Item:
        """
        Retrieves items by call_num for check out.

        :param call_num: string
        :precondition: call_num must be a string
        :return: Item
        """
        return self._retrieve_item_by_call_num(call_num)

    def find_item(self) -> list:
        """
        Find items with the same and similar title.

        :return: a list of titles.
        """
        title = input("Enter title: ")
        title_list = [library_item.title for library_item in self._item_list]
        results = difflib.get_close_matches(title, title_list, cutoff=0.5)
        return results

    def add_item(self):
        """
        Add a brand new item to the library with a unique call number.

        :return: none
        """
        item_type_dict = {ItemType.BOOK: BookFactory,
                          ItemType.DVD: DvdFactory,
                          ItemType.JOURNAL: JournalFactory}

        # ask for item type
        item_type = None
        while True:
            print("\n".join(f"{item.value}. {item.name}" for item in ItemType))
            try:
                item_type = int(input("Select one: "))
            except ValueError:
                continue
            if item_type in [a_type.value for a_type in ItemType]:
                break

        # ask for instance variables for Item object
        title = input("Enter title: ")
        call_num = input("Enter call number: ")
        num_copies = 0
        while True:
            try:
                num_copies = int(input("Enter number of copies: "))
                break
            except ValueError:
                continue

        # check if the item with the same call number exists
        if self._retrieve_item_by_call_num(call_num):
            print(f"Could not add item with call number {call_num}. It already exists. ")
            return

        # create item
        item = item_type_dict[ItemType(item_type)]().create_item(title=title, call_num=call_num, num_copies=num_copies)
        self._item_list.append(item)

    def remove_item(self, call_num: str):
        """
        Remove an existing item from the library.

        :param call_num: a string
        :precondition call_num: a unique identifier
        :return: none
        """
        found_item = self._retrieve_item_by_call_num(call_num)
        if found_item:
            self._item_list.remove(found_item)
            print(f"Successfully removed {found_item.title} with "
                  f"call number: {call_num}")
        else:
            print(f"Item with call number: {call_num} not found.")

    def reduce_item_count(self, call_num: str) -> bool:
        """
        Decrement the book count for an book with the given call number
        in the library.

        :param call_num: a string
        :precondition call_num: a unique identifier
        :return: True if the book was found and count decremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_num(call_num)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_item_count(self, call_num: str) -> bool:
        """
        Increment the book count for an book with the given call number
        in the library.

        :param call_num: a string
        :precondition call_num: a unique identifier
        :return: True if the book was found and count incremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_num(call_num)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False

    def __str__(self) -> str:
        """
        Return the string representation of the class.

        :return: string
        """
        table = Texttable()
        table.add_rows([[item.__str__()] for item in self._item_list])
        table.set_cols_align(["c"])

        return table.draw()
