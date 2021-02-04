class User:
    """
    This class represents a FAM user and their user details.
    """

    def __init__(self, name, age, account, budgets, lock_status):
        """
        Initialize user details.

        :param name: a string
        :param age: an int
        :param account: an Account object
        :param budgets: a tuple of budgets
        :param lock_status: a boolean
        :precondition: name must be a string
        :precondition: age must be an int
        :precondition: account must be an Account
        :precondition: budgets must be a tuple
        :precondition: lock_status must be a bool
        """
        self._name = name
        self._age = age
        self._account = account
        self._budgets = budgets
        self._lock_status = lock_status

    def get_transaction_by_date(self):
        """
        Return string consists of transaction details ordered by date.

        :return: str
        """
        all_transactions = []
        for budget in self._budgets:
            all_transactions += budget.transactions

        all_transactions.sort(key=lambda x: x.timestamp)
        transaction_str = ""
        for transaction in all_transactions:
            transaction_str += transaction.__str__() + "\n"
        return transaction_str

    @property
    def name(self):
        """
        Display only property for _budget.

        :return: str
        """
        return self._name

    @property
    def budgets(self):
        """
        Display only property for _budget.

        :return: float
        """
        return self._budgets

    @property
    def account(self):
        """
        Display only property for _account.

        :return: Account
        """
        return self._account
