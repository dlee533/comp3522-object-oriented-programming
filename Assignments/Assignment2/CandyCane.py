from Candy import Candy
from Colours import Colours
from InvalidDataError import InvalidDataError


class CandyCane(Candy):
    """
    Represents CandyCane, type of candy for Christmas.
    """
    def __init__(self, colour, **kwargs):
        """
        Initializes instance variables.
        :param colour: int, represents a colour in Colours enum
        :param kwargs: key value pairs of contains_nuts, lactose_free, name, description, product_id
        """
        super().__init__(**kwargs)
        colours = {"red": Colours.RED, "green": Colours.GREEN}
        if colour.lower() not in colours.keys():
            raise InvalidDataError(f"Colour can only be \"Red\", or \"Green\"")
        self._colour = colours[colour.lower()]
