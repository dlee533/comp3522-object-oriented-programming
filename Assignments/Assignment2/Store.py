import datetime

from texttable import Texttable

from os import path

from InvalidDataError import InvalidDataError
from OrderProcessor import OrderProcessor


class Store:
    """
    Class that represents a store that sells holiday items.
    """
    def __init__(self):
        """
        Initializes instance variables of Store object.
        """
        self._orders = []
        self._inventory = {}  # {item: quantity}
        self._datetime = datetime.datetime.now()

    def process_orders(self):
        """
        Process orders written on the excel file.
        :return: None
        """
        file_path = input("Enter file path (or press enter if you want to process 'orders.xlsx'): ").strip()
        file_path = "orders.xlsx" if file_path == "" else file_path
        try:
            orders = OrderProcessor.read_order(file_path)
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e.args[0]}")
        except Exception as e:
            print(f"Error: {e.args[0]}")
        else:
            for order in orders:
                self._orders.append(order)
                self.update_inventory(order)
            print("Orders processed!")

    def update_inventory(self, order):
        """
        Update inventory of the store according to the order received.
        :param order: Order
        :return: None
        """
        order_quantity = order.product_details["quantity"]
        inventory = self._inventory
        item = list(filter(lambda product: product.product_id == order.product_id, inventory))

        # if the item doesn't exist in inventory, try get it from factory
        if len(item) != 1:
            try:
                item = self.get_item_from_factory(order)
                self._inventory[item] = 100
            except InvalidDataError as e:
                order.is_valid = False
                order.set_error_msg(e.__str__())
                return
        else:
            item = item[0]

        # if the quantity of the item is less than the order
        if self._inventory[item] < order_quantity:
            self._inventory[item] += 100
        # subtract the inventory quantity by order quantity
        self._inventory[item] -= order_quantity

    @staticmethod
    def get_item_from_factory(order):
        """
        Static method that returns the correct Item object.
        :param order: Order
        :return: Item object if all the product details are valid, else, raise ValueError
        """
        # process product_details dictionary to 1)remove quantity & 2)add name and product_id information
        product_details = dict(order.product_details)
        product_details.pop("quantity")
        product_details["name"] = order.name
        product_details["product_id"] = order.product_id

        # call methods based on the item type, if the item type is not one of (toy, stuffedAnimal, candy), raise error
        item = order.item.lower()
        if item == "toy":
            return order.factory_object.create_toy(**product_details)
        elif item == "stuffedanimal":
            return order.factory_object.create_stuffed_animal(**product_details)
        elif item == "candy":
            return order.factory_object.create_candy(**product_details)
        else:
            raise ValueError("Invalid Order")

    def check_inventory(self):
        """
        Display inventory.
        :return: None
        """
        inventory = self._inventory
        states = {10: "In Stock",
                  3: "Low",
                  1: "Very Low",
                  0: "Out of Stock"}
        inventory_table = Texttable()
        inventory_table.add_rows([["Product ID", "Name", "State"]], header=True)
        for item, quantity in inventory.items():
            state = {min_quantity: state for min_quantity, state in states.items() if min_quantity <= quantity}
            inventory_table.add_row([item.product_id, item.name, state.get(max(state.keys()))])
        inventory_table.set_deco(Texttable.BORDER | Texttable.HEADER | Texttable.VLINES)
        print(inventory_table.draw())

    def create_report(self):
        """
        Create report with order details.
        :return: None
        """
        # store contents of report in text variable
        text = "HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT)\n"
        text += self._datetime.strftime("%d-%m-%Y %H:%M") + "\n"
        text += "\n".join([order.__str__() for order in self._orders])

        # format file name
        base_file_name = self._datetime.strftime("%d%m%Y_%H%M")
        base_file_name = f"DTR_{base_file_name}.txt"
        file_name = base_file_name

        # check if the file with same name exists: in case the program is re executed in the short span of time
        file_num = 1
        while path.exists(file_name):
            file_name = base_file_name.replace(".", f"({file_num}).")
            file_num += 1

        # write report
        with open(file_name, mode="w", encoding="utf-8") as file:
            file.write(text)
            file.write("\n\n")

        print("Report created")

    def display_menu(self):
        """
        Discplay menu and forward user to the appropriate method.
        :return: boolean, whether the program should continue or not
        """
        # display menu and define action
        action_map = {1: self.process_orders,
                      2: self.check_inventory,
                      3: self.create_report}
        menu = Texttable()
        menu.add_rows([["Holiday store menu:"],
                       ["1. Process web orders"],
                       ["2. Check inventory"],
                       ["3. Exit"]])
        menu.set_deco(Texttable.BORDER | Texttable.HEADER)
        print(menu.draw())

        # get user's input
        user_input = 0
        while user_input not in range(1, 4):
            try:
                user_input = int(input("Enter a number between 1~3: "))
            except ValueError:
                pass  # input prompt is clear, additional message is not needed

        action_map[user_input]()

        return True if user_input in (1, 2) else False
