from Item import Item


class Candy(Item):
    """
    Representation of Candy.
    """
    def __init__(self, has_nuts, has_lactose, **kwargs):
        """
        Initialize instance variables.
        :param has_nuts: boolean
        :param has_lactose: boolean
        """
        super().__init__(**kwargs)
        self._has_nuts = has_nuts
        self._has_lactose = has_lactose
