class Order:
    """
    Class that represents an order received.
    """
    def __init__(self, order_number, product_id, item, name, factory_object, **product_details):
        """
        Initializes Order object.
        :param order_number: int
        :param product_id: string, combination of alphabet and numbers
        :param item: string in (toy, candy, stuffed animal)
        :param name: string, name of the item
        :param factory_object: ItemFactory
        :param product_details: dictionary of key/value pairs of product details used to create item
        """
        self._order_number = order_number
        self._product_id = product_id
        self._item = item
        self._name = name
        self._factory_object = factory_object
        self._product_details = product_details
        self._is_valid = True
        self._error_msg = ""

    @property
    def product_id(self):
        """
        Getter for product_id.
        :return: string
        """
        return self._product_id

    @property
    def item(self):
        """
        Getter for item.
        :return: string
        """
        return self._item

    @property
    def name(self):
        """
        Getter for name.
        :return: string
        """
        return self._name

    @property
    def factory_object(self):
        """
        Getter for factory_object
        :return: ItemFactory
        """
        return self._factory_object

    @property
    def product_details(self):
        """
        Getter for product details.
        :return: dict
        """
        return self._product_details

    def get_is_valid(self):
        """
        Getter for is_valid.
        :return: boolean
        """
        return self._is_valid

    def set_is_valid(self, is_valid):
        """
        Setter for is_valid.
        :param is_valid: boolean
        :return: None
        """
        self._is_valid = is_valid

    is_valid = property(get_is_valid, set_is_valid)

    def set_error_msg(self, error_msg):
        """
        Setter for error_msg.
        :param error_msg: string
        :return: None
        """
        self._error_msg = error_msg

    def __str__(self):
        """
        String representation of the Order object.
        :return: the description of the Order object in readable format
        """
        if self._is_valid:
            quantity = self._product_details.get("quantity")
            return f"Order {self._order_number}, " \
                   f"Item {self._item}, " \
                   f"Product ID {self._product_id}, " \
                   f"Name \"{self._name}\", " \
                   f"Quantity {quantity}"
        else:
            return f"Order {self._order_number}, " \
                   f"{self._error_msg}"
