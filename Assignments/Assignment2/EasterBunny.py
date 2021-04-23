from Colours import Colours
from InvalidDataError import InvalidDataError
from StuffedAnimal import StuffedAnimal


class EasterBunny(StuffedAnimal):
    """
    Represents an Easter Bunny, a Stuffed Animal for Easter.
    """
    def __init__(self, colour, **kwargs):
        """
        Initialize Easter Bunny details.
        :param colour: an enum from Colours enum
        :param kwargs: key-value pairs of stuffing, size, fabric, name, description, product_id
        """
        super().__init__(**kwargs)
        colours = {"blue": Colours.BLUE, "pink": Colours.PINK, "white": Colours.WHITE,
                   "grey": Colours.GREY}
        if colour.lower() not in colours.keys():
            raise InvalidDataError(f"Colour can only be \"Blue\", \"Pink\", \"White\", or \"Grey\"")
        self._colour = colours[colour.lower()]
