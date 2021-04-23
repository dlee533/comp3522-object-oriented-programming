from InvalidDataError import InvalidDataError
from Item import Item
from StuffedAnimalAttributes import StuffedAnimalAttributes


class StuffedAnimal(Item):
    """
    Representation of Stuffed Animal.
    """
    def __init__(self, stuffing, size, fabric, **kwargs):
        """
        Initialize Stuffed Animal instance details.
        :param stuffing: an enum from StuffedAnimalAttributes enum
        :param size: an enum from StuffedAnimalAttributes enum
        :param fabric: an enum from StuffedAnimalAttributes enum
        """
        super().__init__(**kwargs)
        self._stuffing = False
        self._size = False
        self._fabric = False

        stuffing = stuffing.upper().replace(" ", "_")
        for attribute in StuffedAnimalAttributes:
            if attribute.name == stuffing and attribute.value in range(StuffedAnimalAttributes.STUFFING_BEGIN.value,
                                                                       StuffedAnimalAttributes.STUFFING_END.value):
                self._stuffing = attribute
                break
        if not self._stuffing:
            raise InvalidDataError(f"Stuffing can only be \"Polyester Fibrefill\" or \"Wool\"")

        size = size.upper().replace(" ", "_")
        for attribute in StuffedAnimalAttributes:
            if attribute.name == size and attribute.value in range(StuffedAnimalAttributes.SIZE_BEGIN.value,
                                                                   StuffedAnimalAttributes.SIZE_END.value):
                self._size = attribute
                break
        if not self._size:
            raise InvalidDataError(f"Size can only be \"Small\" or \"Medium\" or \"Large\"")

        fabric = fabric.upper().replace(" ", "_")
        for attribute in StuffedAnimalAttributes:
            if attribute.name == fabric and attribute.value in range(StuffedAnimalAttributes.FABRIC_BEGIN.value,
                                                                     StuffedAnimalAttributes.FABRIC_END.value):
                self._fabric = attribute
                break
        if not self._fabric:
            raise InvalidDataError(f"Fabric can only be \"Linen\" or \"Cotton\" or \"Acrylic\"")
