"""
  (7 Marks)
  In this program we are simulating a Landlord taking taking rent from a Tenant.
  The existing code is designed incorrectly.

   Your task is to:
       TODO
       Examine the code below. After examination, answer which design idiom
       the code in this file violates? Write your answer in the space below:

       Answer: Law of Demeter: landlord is accessing tenant's bank account directly from his


       TODO
       Rewrite the code in this file to prevent the violation of the design idiom.
       Ensure you get the following output:

        Before:
        Tenant has $999
        Landlord has $0
        After landlord gets money from tenant:
        Tenant has $899
        Landlord has $100

"""


class BankAccount:
    def __init__(self):
        self._money = 999

    def view_money(self):
        return self._money

    def remove(self, money):
        self._money -= money


class Tenant:
    def __init__(self):
        self._bank_account = BankAccount()

    def pay_rent(self, amount):
        self._bank_account.remove(amount)

    def __str__(self):
        return "Tenant has ${}".format(self._bank_account.view_money())


class Landlord:
    def __init__(self, tenant):
        self._money = 0
        self._tenant = tenant

    def get_tenant(self):
        return self._tenant

    def add_money(self, money):
        self._money += money

    def __str__(self):
        return "Landlord has ${}".format(self._money)


tenant = Tenant()
landlord = Landlord(tenant)

print("Before:")
print(tenant)
print(landlord)

rent = 100
tenant.pay_rent(rent)
landlord.add_money(rent)

print("After landlord gets money from tenant:")
print(tenant)
print(landlord)
