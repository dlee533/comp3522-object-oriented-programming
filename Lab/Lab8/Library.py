from texttable import Texttable

from Lab.Lab8.Catalogue import Catalogue


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

    def check_out(self, call_num):
        """
        Check out an item with the given call number from the library.

        :param call_num: a string
        :precondition call_num: a unique identifier
        :return: none
        """
        library_item = self._catalogue.retrieve_item_for_check_out(call_num)

        if library_item is None:
            print(f"Could not find item with call number {call_num}. Checkout failed.")
            return

        if library_item.check_availability():
            status = self._catalogue.reduce_item_count(call_num)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find item with call number {call_num}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_num}"
                  f". Checkout failed.")

    def return_item(self, call_num):
        """
        Return an item with the given call number from the library.

        :param call_num: a string
        :precondition call_num: a unique identifier
        :return: none
        """
        status = self._catalogue.increment_item_count(call_num)
        if status:
            print("item returned successfully!")
        else:
            print(f"Could not find item with call number {call_num}. Return failed.")

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
        action_dict = {1: self.display_available_items,
                       2: self.check_out,
                       3: self.return_item,
                       4: self._catalogue.find_item,
                       5: self._catalogue.add_item,
                       6: self._catalogue.remove_item}
        user_input = None
        while user_input != 7:
            # ask user to pick an action
            table = Texttable().add_rows(list([f"{key}. {value.__name__.replace('_', ' ').capitalize()}"]
                                              for key, value in action_dict.items()))
            table.add_row([f"7. Quit"])
            table.set_deco(Texttable.BORDER)
            print(table.draw())
            try:
                user_input = int(input("Please enter your choice (1-7): "))
            except ValueError:
                continue

            # if user input is valid
            if user_input in action_dict.keys():
                if user_input in (2, 3, 6):
                    call_num = input("Enter the call number: ")
                    action_dict[user_input](call_num)
                elif user_input == 4:
                    found = action_dict[user_input]()
                    if user_input == 4:
                        if len(found) > 0:
                            print("\n".join(title for title in found))
                        else:
                            print("Sorry! We found nothing with that title")
                else:
                    action_dict[user_input]()
                input("press enter to continue")
