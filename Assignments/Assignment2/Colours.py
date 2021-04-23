from enum import Enum, auto


class Colours(Enum):
    """
    Represents colours of particular store items that come in different colours (Robot Bunny,
    Easter Bunny, Candy Cane).
    """
    ROBOT_BUNNY_BEGIN = ORANGE = auto()
    EASTER_BUNNY_BEGIN = BLUE = auto()
    PINK = auto()
    ROBOT_BUNNY_END = WHITE = auto()
    GREY = auto()
    EASTER_BUNNY_END = CHRISTMAS_BEGIN = RED = auto()
    GREEN = auto()
