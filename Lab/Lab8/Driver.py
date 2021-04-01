from Lab.Lab8.Book import Book
from Lab.Lab8.Library import Library


def generate_test_books():
    """
    Return a list of books with dummy data.

    :return: a list
    """
    book_list = [
        Book(call_num="100.200.300", title="Harry Potter 1", num_copies=2, author="J K Rowling"),
        Book(call_num="999.224.854", title="Harry Potter 2", num_copies=5, author="J K Rowling"),
        Book(call_num="631.495.302", title="Harry Potter 3", num_copies=4, author="J K Rowling"),
        Book(call_num="123.02.204", title="The Cat in the Hat", num_copies=1, author="Dr. Seuss")
    ]
    return book_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    print("\nWelcome to the Library!")
    book_list = generate_test_books()
    my_epic_library = Library(book_list)
    my_epic_library.display_library_menu()
    print("Thank you for visiting the Library.")


if __name__ == '__main__':
    main()
