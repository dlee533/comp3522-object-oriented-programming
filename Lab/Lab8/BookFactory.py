from ItemFactory import ItemFactory
from Book import Book


class BookFactory(ItemFactory):
    """
    Responsible for creating Book objects.
    """
    def create_item(self, **kwargs):
        """
        Return a Book object.
        :param kwargs: key-value pairs consisting of call_num, title, num_copies details
        :return: Book object
        """
        author = input("Enter author name: ")
        return Book(author, **kwargs)
