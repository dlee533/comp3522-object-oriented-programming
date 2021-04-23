from Candy import Candy


class CremeEgg(Candy):
    """
    Represents CremeEgg, type of candy for Christmas.
    """
    def __init__(self, pack_size, **kwargs):
        """
        Initializes instance variables.
        :param pack_size: int
        :param kwargs: key value pairs of has_nuts, has_lactose, name, description, product_id
        """
        super().__init__(**kwargs)
        self._pack_size = pack_size
