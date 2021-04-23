from RobotBunny import RobotBunny
from EasterBunny import EasterBunny
from CremeEgg import CremeEgg
from ItemFactory import ItemFactory


class EasterFactory(ItemFactory):
    """
    Factory class for Easter items.
    """
    def create_toy(self, **kwargs):
        """
        Returns RobotBunny object.
        :param kwargs: key value pairs necessary to initialize RobotBunny object
        :return: RobotBunny
        """
        return RobotBunny(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """
        Returns EasterBunny object.
        :param kwargs: key value pairs necessary to initialize EasterBunny object
        :return: EasterBunny
        """
        return EasterBunny(**kwargs)

    def create_candy(self, **kwargs):
        """
        Returns CremeEgg object.
        :param kwargs: key value pairs necessary to initialize CremeEgg object
        :return: CremeEgg
        """
        return CremeEgg(**kwargs)
