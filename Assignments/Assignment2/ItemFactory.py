import abc


class ItemFactory(abc.ABC):
    """
    Abstract factory class.
    """
    @abc.abstractmethod
    def create_toy(self, **kwargs):
        """
        Returns toy object.
        :param kwargs: key value pairs necessary to initialize toy object
        :return: toy object, depends on the implementation
        """
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self, **kwargs):
        """
        Returns stuffed_animal object.
        :param kwargs: key value pairs necessary to initialize stuffed_animal object
        :return: stuffed_animal object, depends on the implementation
        """
        pass

    @abc.abstractmethod
    def create_candy(self, **kwargs):
        """
        Returns candy object.
        :param kwargs: key value pairs necessary to initialize candy object
        :return: candy object, depends on the implementation
        """
        pass
