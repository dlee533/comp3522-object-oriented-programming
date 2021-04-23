import abc


class Item(abc.ABC):
    """
    Abstract representation of an Item
    """

    def __init__(self, name, description, product_id):
        """
        Initializes variables.
        :param name: string
        :param description: string
        :param product_id: string
        """
        print("Item")
        self._name = name
        self._description = description
        self._product_id = product_id

    @property
    def name(self):
        """
        Getter for name.
        :return: name, string
        """
        return self._name

    @property
    def product_id(self):
        """
        Getter for product_id.
        :return: product_id, string
        """
        return self._product_id
