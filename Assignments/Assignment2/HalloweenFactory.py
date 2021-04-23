from ItemFactory import ItemFactory
from PumpkinCaramelToffee import PumpkinCaramelToffee
from RCSpider import RCSpider
from DancingSkeleton import DancingSkeleton


class HalloweenFactory(ItemFactory):
    """
    Factory class for Halloween items.
    """
    def create_toy(self, **kwargs):
        """
        Returns RCSpider object.
        :param kwargs: key value pairs necessary to initialize RCSpider object
        :return: RCSpider
        """
        return RCSpider(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """
        Returns DancingSkeleton object.
        :param kwargs: key value pairs necessary to initialize DancingSkeleton object
        :return: DancingSkeleton
        """
        return DancingSkeleton(**kwargs)

    def create_candy(self, **kwargs):
        """
        Returns PumpkinCaramelToffee object.
        :param kwargs: key value pairs necessary to initialize PumpkinCaramelToffee object
        :return: PumpkinCaramelToffee
        """
        return PumpkinCaramelToffee(**kwargs)
