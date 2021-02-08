from lab4.Account import Account
from lab4.Budget import Budget
from lab4.Category import Category
from lab4.Moderator import Moderator
from lab4.User import User


def load_test_user():
    """
    Loads test user.
    """
    test_budgets = (Budget(Category.ENTERTAINMENT, 100), Budget(Category.CLOTHING, 100), Budget(Category.FOOD, 100),
                    Budget(Category.MISC, 100))
    test_account = Account("A_Bank", "1234567890", 1000)
    test_user = User("A_Name", 15, test_account, test_budgets, True)
    application = Moderator(test_user)

    # test_transaction1 = Transaction(datetime.fromtimestamp(time.time()), 50, 2, "transaction1")
    # test_transaction2 = Transaction(datetime.fromtimestamp(10000), 30, 1, "transaction2")
    # test_transaction3 = Transaction(datetime.fromtimestamp(10000000), 1, 1, "transaction2")
    # test_budgets[1].add_transaction(test_transaction1)
    # test_budgets[0].add_transaction(test_transaction2)
    # test_budgets[0].add_transaction(test_transaction3)

    while True:
        application.display_menu()


def main():
    load_test_user()


if __name__ == "__main__":
    main()
