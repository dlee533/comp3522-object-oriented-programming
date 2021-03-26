import abc


class ItemFactory(abc.ABC):
    """
    Abstract factory class for creating items.
    """
    @abc.abstractmethod
    def create_item(self):
        """
        Create an item.
        :return: None (abstract method)
        """
        pass

