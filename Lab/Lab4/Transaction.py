from lab4.Category import Category


class Transaction:
    """
    Represents a transaction and its details.
    """
    def __init__(self, timestamp, amount, budget_category, vendor_name):
        """
        Initialize a transaction.

        :param timestamp: a datetime object
        :param amount: a float
        :param budget_category: an enum
        :param vendor_name: a string
        :precondition: timestamp must be a Datetime
        :precondition: amount must be a float
        :precondition: budget_category must be an enum
        :precondition: vendor_name must be a string
        """
        self._timestamp = timestamp
        self._amount = amount
        self._budget_category = budget_category
        self._vendor_name = vendor_name

    @property
    def amount(self):
        """
        Display only property for _amount.

        :return: float
        """
        return self._amount

    @property
    def timestamp(self):
        """
        Display only property for _timestamp.

        :return: Datetime
        """
        return self._timestamp

    def __str__(self):
        """
        Return string description of the Transaction object.

        :return: formatted string of Transaction details
        """
        return f"---- Recorded transaction time: {self._timestamp} ----\n" \
               f"Transaction amount: ${self._amount:.2f}\n" \
               f"Budget category: {Category(self._budget_category)}\n" \
               f"Store/website name: {self._vendor_name}"
