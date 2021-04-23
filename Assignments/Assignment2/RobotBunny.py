from Colours import Colours
from InvalidDataError import InvalidDataError
from Toy import Toy


class RobotBunny(Toy):
    """
    Represents a Robot Bunny, an Toy for Easter.
    """
    def __init__(self, num_sound, colour, **kwargs):
        """
        Initialize Robot Bunny details.

        :param num_sound: an integer
        :param colour: an enum from Colours enum
        :param kwargs: key value pairs of battery_operated, min_recommended_age, name,
        description, and product_id
        """
        super().__init__(**kwargs)
        self._num_sound = num_sound
        colours = {"orange": Colours.ORANGE, "blue": Colours.BLUE, "pink": Colours.PINK}
        if colour.lower() not in colours.keys():
            raise InvalidDataError(f"Colour can only be \"Orange\", \"Blue\", or \"Pink\"")
        self._colour = colours[colour.lower()]
