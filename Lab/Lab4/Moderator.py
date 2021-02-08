from datetime import datetime
import time

from lab4.Category import Category
from lab4.Transaction import Transaction


class Moderator:
    """
    This class provides an interface for users to manage their Family Appointed Moderator (FAM) account.
    """
    def __init__(self, *args):
        """
        Initialize FAM users.

        :param args: User object(s)
        :precondition: args must be User object(s)
        """
        self._users = list(args)

    @staticmethod
    def _select_category():
        """
        Asks user to choose a category.

        :return: int
        """
        print("Categories".center(25, '-'))
        print("1. Games and Entertainment")
        print("2. Clothing and Accessories")
        print("3. Eating Out")
        print("4. Miscellaneous")
        print("".center(25, '-'))
        category = int(input("Select one: "))
        if category in range(1, 5):
            return category
        else:
            return 0

    @staticmethod
    def _view_account_detail(user):
        """
        Display the details of a user's bank account and transactions made ordered by date

        :param user: User
        :precondition: user must be a User
        :return: None
        """
        print(user.account)
        print(user.get_transaction_by_date())

    def register_user(self, user):
        """
        Register a user in to the moderator.

        :param user: User
        :precondition: user must be a User
        :return: None
        """
        self._users.append(user)

    def display_menu(self):
        """
        Display menu.

        :return: None
        """
        print("Users".center(25, "-"))
        for i in range(len(self._users)):
            user = self._users[i]
            print(f"{i + 1}. {user.name}")
        print("".center(25, "-"))
        user_index = int(input("Enter a number: ")) - 1
        user = self._users[user_index]

        menu_input = 0
        while menu_input != 5:
            print("Options".center(25, "-"))
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions by Budget")
            print("4. View Bank Account Details")
            print("5. Logout")
            print("".center(25, "-"))
            menu_input = int(input("Enter a number: "))
            if menu_input == 1:
                self._view_budgets(user)
            elif menu_input == 2:
                self._record_transaction(user)
            elif menu_input == 3:
                self._view_budget_transaction(user)
            elif menu_input == 4:
                self._view_account_detail(user)
            elif menu_input == 5:
                return
            else:
                print("Invalid input")

    def _view_budgets(self, user):
        """
        Display budget detail of selected category.

        :param user: User
        :precondition: user must be a User
        :return: None
        """
        category = self._select_category()
        print(user.budgets[category - 1])

    def _record_transaction(self, user):
        """
        Record and display new transaction(s) made by the user.

        :param user: a User instance
        :precondition: user must be a User
        :return: None
        """
        new_transactions = []
        while True:
            budgets = user.budgets
            timestamp = datetime.fromtimestamp(time.time())
            budget_category = self._select_category()
            if not budget_category:
                print("Invalid value")
                continue
            elif budgets[budget_category - 1].lock_status:
                print(f"{Category(budget_category)} is locked")
                continue

            print("".center(25, "-"))
            vendor_name = input("Enter the vendor name: ")
            amount = float(input("Enter dollar amount: "))
            transaction = Transaction(timestamp, amount, budget_category, vendor_name)
            budgets[budget_category - 1].add_transaction(transaction)
            new_transactions.append(transaction)
            print("".center(25, '-'))
            account = user.account
            account.decrease_balance(amount)
            if input("Exit(y/n): ") == "y":
                for new_transaction in new_transactions:
                    print(new_transaction)
                return

    def _view_budget_transaction(self, user):
        """
        Display transaction of a budget.

        :param user: User
        :precondition: user must be a User
        :return: None
        """
        category = self._select_category()
        if category not in range(1, 5):
            print("Incorrect input")
            return
        print(user.budgets[category - 1])
