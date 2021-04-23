from Candy import Candy
from CandyVariety import CandyVariety
from InvalidDataError import InvalidDataError


class PumpkinCaramelToffee(Candy):
    """
    Represents PumpkinCaramelToffee, type of candy for Halloween.
    """
    def __init__(self, variety, **kwargs):
        """
        Initializes instance variables.
        :param variety: int, represents a candy variety in CandyVariety enum
        :param kwargs: key value pairs of has_nuts, has_lactose, name, description, product_id
        """
        super().__init__(**kwargs)
        varieties = {"sea salt": CandyVariety.SEA_SALT,
                     "regular": CandyVariety.REGULAR}
        if variety.lower() not in varieties.keys():
            raise InvalidDataError(f"Variety can only be \"Sea Salt\" or \"Regular\"")
        self._variety = varieties[variety.lower()]
