class Account:
    """
    Represents a user's bank account and the balance.
    """

    def __init__(self, bank_name, account_num, balance):
        """
        Initialize the user's bank account details.

        :param bank_name: a string
        :param account_num: a string
        :param balance: a float
        :precondition: bank_name must be a string
        :precondition: account_num must be a string
        :precondition: balance must be a float
        """
        self._bank_name = bank_name
        self._account_num = account_num
        self._balance = balance

    def decrease_balance(self, amount):
        self._balance -= amount

    def __str__(self):
        """
        Return string of Account details.

        :return: formatted string of Account details
        """
        return f"bank name: {self._bank_name}\n" \
               f"account_num: {self._account_num}\n" \
               f"balance: {self._balance}"
