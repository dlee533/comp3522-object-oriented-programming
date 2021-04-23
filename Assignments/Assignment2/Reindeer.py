from StuffedAnimal import StuffedAnimal


class Reindeer(StuffedAnimal):
    """
    Represents a Reindeer, a Stuffed Animal for Christmas.
    """
    def __init__(self, has_glow, **kwargs):
        """
        Initialize Reindeer instance details.
        :param has_glow: boolean
        :param kwargs: key-value pairs of stuffing, size, fabric, name, description, product_id
        """
        super().__init__(**kwargs)
        self._has_glow = has_glow
