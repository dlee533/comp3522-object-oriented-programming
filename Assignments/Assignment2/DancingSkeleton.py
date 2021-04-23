from StuffedAnimal import StuffedAnimal


class DancingSkeleton(StuffedAnimal):
    """
    Represents a Dancing Skeleton, a Stuffed Animal for Halloween.
    """

    def __init__(self, has_glow, **kwargs):
        """
        Initialize Dancing Skeleton details.
        :param has_glow: boolean
        :param kwargs: key-value pairs of stuffing, size, fabric, name, description, product_id
        """
        super().__init__(**kwargs)
        self._has_glow = has_glow
