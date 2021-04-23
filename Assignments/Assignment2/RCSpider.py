from InvalidDataError import InvalidDataError
from SpiderTypes import SpiderTypes
from Toy import Toy


class RCSpider(Toy):
    """
    Represents an Remote-Controlled (RC) Spider, a Toy for Halloween.
    """
    def __init__(self, speed, jump_height, has_glow, spider_type, **kwargs):
        """
        Initialize RCSpider details.
        :param speed: a float
        :param jump_height: a float
        :param has_glow: a boolean
        :param spider_type: an enum from SpiderTypes enum
        :param kwargs: key value pairs of battery_operated, min_recommended_age, name,
        description, and product_id
        """
        super().__init__(**kwargs)
        self._speed = speed
        self._jump_height = jump_height
        self._has_glow = has_glow
        spider_types = {"tarantula": SpiderTypes.TARANTULA,
                        "wolf spider": SpiderTypes.WOLF_SPIDER}
        if spider_type.lower() not in spider_types.keys():
            raise InvalidDataError(f"Variety can only be \"Sea Salt\" or \"Regular\"")
        self._spider_type = spider_types[spider_type.lower()]
