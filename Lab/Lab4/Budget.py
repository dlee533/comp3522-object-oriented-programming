from Lab.Lab4.Category import Category


class Budget:
    """
    Represents a budget for a user.
    """
    NOTIFY = 0.5
    WARN = 0.75
    LOCK = 1

    def __init__(self, category, total_amount):
        """
        Initialize details of a user's budget.

        :param category: an enum
        :param total_amount: a float
        :precondition: category must be an enum
        :precondition: total_amount must be a float
        """
        self._category = category
        self._total_amount = total_amount
        self._amount_spent = 0
        self._amount_left = total_amount
        self._lock_status = True if self._amount_left <= 0 else False
        self._transactions = []

    def add_transaction(self, transaction):
        """
        Add transaction to the transaction list.

        :param transaction: Transaction
        :precondition: transaction must be a Transaction
        :return: None
        """
        self._amount_left -= transaction.amount
        self._amount_spent += transaction.amount
        new_spent_ratio = self._amount_spent / self._total_amount
        if new_spent_ratio >= self.LOCK:
            print(f"LOCKED!!! you used {int(new_spent_ratio * 100)}% of your budget!!!")
            self._lock_status = True
        elif new_spent_ratio >= self.WARN:
            print(f"WARNING! you used {int(new_spent_ratio * 100)}% of your budget!")
        elif new_spent_ratio >= self.NOTIFY:
            print(f"Notification: you used {int(new_spent_ratio * 100)}% of your budget")
        self._transactions.append(transaction)

    @property
    def lock_status(self):
        """
        Display only property for _lock_status.

        :return: bool
        """
        return self._lock_status

    @property
    def transactions(self):
        """
        Display only property for _transaction.

        :return: Transaction
        """
        return self._transactions

    def __str__(self):
        """
        Returns string representation of the object.

        :return: str
        """
        my_str = f"{Category(self._category)}".center(50, '-')
        my_str += f"\nLock Status: {self._lock_status}\n" \
                  f"Total Amount: {self._total_amount}\n" \
                  f"Amount Spent: {self._amount_spent}\n" \
                  f"Amount_Left: {self._amount_left}\n" \
                  f"Transactions:\n"
        for transaction in self._transactions:
            my_str += f"\t{transaction.__str__()}\n"

        my_str += "".center(50, '-')
        return my_str
