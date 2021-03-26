from ItemFactory import ItemFactory
from Journal import Journal


class JournalFactory(ItemFactory):
    """
    Responsible for creating Journal objects.
    """
    def create_item(self, **kwargs):
        """
        Return a Journal object.
        :param kwargs: key-value pairs consisting of call_num, title, num_copies details
        :return: Journal object
        """
        name = input("Enter journal name: ")
        while True:
            try:
                issue_number = int(input("Enter issue number: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
            else:
                break
        publisher = input("Enter publisher name: ")
        return Journal(name, issue_number, publisher, **kwargs)
