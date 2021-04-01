from Lab.Lab8.Item import Item


class Dvd(Item):
    """
    Represents a single DVD in catalogue which is identified through its call number.
    """

    def __init__(self, release_date: str, region_code: str, **kwargs):
        """
        Initializes a Dvd.

        :param release_date: a string
        :param region_code: a string
        :param **kwargs: key value pair for initializing Item
        """
        super().__init__(**kwargs)
        self._release_date = release_date
        self._region_code = region_code

    def __str__(self) -> str:
        """
        Return string description of object.

        :return: string
        """
        return f"DVD: {self._title}\n" \
               f"Call Number: {self._call_num}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Release Date: {self._release_date}\n" \
               f"Region Code: {self._region_code}"
