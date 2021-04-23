from Toy import Toy


class SantasWorkshop(Toy):
    """
    Represents Santa's Workshop, a Toy for Christmas.
    """
    def __init__(self, dimensions, num_rooms, **kwargs):
        """
        Initialize Santa's Workshop details.

        :param dimensions: a tuple with values representing width and height of the Toy
        :param num_rooms: an integer
        :param kwargs: key value pairs of battery_operated, min_recommended_age, name,
        description, and product_id
        """
        super().__init__(**kwargs)
        self._dimensions = dimensions
        self._num_rooms = num_rooms
