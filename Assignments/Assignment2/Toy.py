from Item import Item


class Toy(Item):
    """
    Representation of Toy.
    """
    def __init__(self, has_batteries, min_age, **kwargs):
        """
        Initialize Toy instance details.
        :param has_batteries: a boolean
        :param min_age: an integer
        """
        super().__init__(**kwargs)
        self._has_batteries = has_batteries
        self._min_age = min_age
