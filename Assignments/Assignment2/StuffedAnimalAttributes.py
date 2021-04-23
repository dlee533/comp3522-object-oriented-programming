from enum import Enum, auto


class StuffedAnimalAttributes(Enum):
    """
    Represents the varieties for particular attributes of a Stuffed Animal (various stuffing,
    fabric, and size types).
    """
    POLYESTER_FIBREFILL = STUFFING_BEGIN = auto()
    WOOL = auto()
    LINEN = STUFFING_END = FABRIC_BEGIN = auto()
    COTTON = auto()
    ACRYLIC = auto()
    S = FABRIC_END = SIZE_BEGIN = auto()
    M = auto()
    L = auto()
    SIZE_END = auto()
