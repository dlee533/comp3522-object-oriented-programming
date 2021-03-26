from Lab8.Item import Item


class Journal(Item):
    """
    Represents a single scientific journal in catalogue which is identified through its call number.
    """

    def __init__(self, name: str, issue_number: int, publisher: str, **kwargs):
        """
        Initializes a journal.

        :param name: a string
        :param issue_number: an int
        :param publisher: a string
        :param **kwargs: key value pair for initializing Item
        """
        super().__init__(**kwargs)
        self._name = name
        self._issue_number = issue_number
        self._publisher = publisher

    def __str__(self) -> str:
        """
        Return string description of object.

        :return: string
        """
        return f"Journal: {self._title}\n" \
               f"Call Number: {self._call_num}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}"
