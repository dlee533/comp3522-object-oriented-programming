""" This module houses the library"""
from book import Book, Journal, Dvd, Item
import difflib
import datetime


class Library:
    """
    The Library provides an interface for users to check out, return, and find books.
    """

    def __init__(self, item_list: list):
        """
        Initialize a catalogue.
        :param item_list: a Catalogue object
        :precondition: item_list must be a list
        """
        self._catalogue = Catalogue(item_list)

    def check_out(self, call_number: str):
        """
        Check out an item with the given call number from the library.

        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: none
        """
        library_item = self._catalogue.retrieve_item_for_check_out(call_number)

        if library_item.check_availability():
            status = self._catalogue.reduce_item_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find item with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_item(self, call_number: str):
        """
        Return an item with the given call number from the library.

        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: none
        """
        status = self._catalogue.increment_item_count(call_number)
        if status:
            print("item returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Return failed.")

    def display_available_items(self):
        """
        Display all the books in the library.

        :return: none
        """
        print(self._catalogue)

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of items, check out, return, find, add, remove an item.

        :return: none
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.display_available_items()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out.")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return.")
                self.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item:")
                found_titles = self._catalogue.find_items(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self._catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the item")
                self._catalogue.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")


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

    def _retrieve_item_by_call_number(self, call_number: str) -> Item:
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the library.

        :param call_number: a string
        :precondition: call_number must be a string
        :return: item object if found, None otherwise
        """
        found_item = None
        for library_item in self._item_list:
            if library_item.call_number == call_number:
                found_item = library_item
                break
        return found_item

    def retrieve_item_for_check_out(self, call_number: str) -> Item:
        """
        Retrieves items by call_number for check out.

        :param call_number: string
        :precondition: call_num must be a string
        :return: Item
        """
        return self._retrieve_item_by_call_number(call_number)

    def find_items(self, title: str) -> list:
        """
        Find items with the same and similar title.

        :param title: a string
        :precondition: title must be a string
        :return: a list of titles.
        """
        title_list = []
        for library_item in self._item_list:
            title_list.append(library_item.get_title())
        results = difflib.get_close_matches(title, title_list, cutoff=0.5)
        return results

    def add_item(self):
        """
        Add a brand new item to the library with a unique call number.

        :return: none
        """
        item = LibraryItemGenerator.create_item()

        found_item = self._retrieve_item_by_call_number(item.call_number)
        if found_item:
            print(f"Could not add item with call number "
                  f"{item.call_number}. It already exists. ")
        else:
            self._item_list.append(item)

    def remove_item(self, call_number: str):
        """
        Remove an existing item from the library.

        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: none
        """
        found_item = self._retrieve_item_by_call_number(call_number)
        if found_item:
            self._item_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"Item with call number: {call_number} not found.")

    def reduce_item_count(self, call_number: str) -> bool:
        """
        Decrement the book count for an book with the given call number
        in the library.

        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count decremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_item_count(self, call_number: str) -> bool:
        """
        Increment the book count for an book with the given call number
        in the library.

        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count incremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
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
        my_str = "Items List\n" \
                 "--------------\n\n"
        for item in self._item_list:
            my_str += item.__str__() + "\n"

        return my_str


class LibraryItemGenerator:
    """
    Responsible for creating library items according to user input of item type.
    """

    @staticmethod
    def create_item():
        """
        Create item with information from user input.

        :return: item created
        """
        call_num = input("Enter Call Number: ")
        title = input("Enter item title: ")
        num_copies = int(input("Enter number of copies (positive number): "))
        item_data = (call_num, title, num_copies)

        while True:
            item_type = input("Enter item type: ")
            if item_type in ["book", "journal", "dvd"]:
                break

        if item_type == "book":
            item = LibraryItemGenerator.create_book(item_data)
        elif item_type == "journal":
            item = LibraryItemGenerator.create_journal(item_data)
        else:
            item = LibraryItemGenerator.create_dvd(item_data)

        return item

    @staticmethod
    def create_book(book_data: tuple) -> Book:
        """
        Create book from user input.

        :param book_data: a tuple
        :precondition: book_data is a tuple with three string values
        :return: Book object
        """
        author = input("Enter author name: ")
        new_book = Book(book_data[0], book_data[1], book_data[2], author)
        return new_book

    @staticmethod
    def create_journal(journal_data: tuple) -> Journal:
        """
        Create journal from user input.

        :param journal_data: a tuple
        :precondition: journal_data is a tuple with three string values
        :return: Journal object
        """
        name = input("Enter journal name: ")
        issue_number = int(input("Enter issue number: "))
        publisher = input("Enter publisher name: ")
        new_journal = Journal(journal_data[0], journal_data[1], journal_data[2], name, issue_number, publisher)
        return new_journal

    @staticmethod
    def create_dvd(dvd_data: tuple) -> Dvd:
        """
        Create dvd from user input.

        :param dvd_data: a tuple
        :precondition: dvd_data is a tuple with three string values
        :return: Dvd object
        """
        release_date = datetime.date.fromisoformat(input("Enter release date (yyyy-mm-dd): "))
        region_code = input("Enter region code: ")
        new_dvd = Dvd(dvd_data[0], dvd_data[1], dvd_data[2], release_date, region_code)
        return new_dvd


def generate_test_books():
    """
    Return a list of books with dummy data.

    :return: a list
    """
    book_list = [
        Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss")
    ]
    return book_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    book_list = generate_test_books()
    my_epic_library = Library(book_list)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
