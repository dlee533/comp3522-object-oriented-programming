from CandyCane import CandyCane
from SantasWorkshop import SantasWorkshop
from Reindeer import Reindeer
from ItemFactory import ItemFactory


class ChristmasFactory(ItemFactory):
    """
    Factory class for Christmas items.
    """
    def create_toy(self, **kwargs):
        """
        Returns SantasWorkshop object.
        :param kwargs: key value pairs necessary to initialize SantasWorkshop object
        :return: SantasWorkshop
        """
        return SantasWorkshop(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """
        Returns Reindeer object.
        :param kwargs: key value pairs necessary to initialize Reindeer object
        :return: Reindeer
        """
        return Reindeer(**kwargs)

    def create_candy(self, **kwargs):
        """
        Returns CandyCane object.
        :param kwargs: key value pairs necessary to initialize CandyCane object
        :return: CandyCane
        """
        return CandyCane(**kwargs)
