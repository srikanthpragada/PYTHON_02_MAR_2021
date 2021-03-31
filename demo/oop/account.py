class FundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Insufficient Funds. Available Balance = {self.balance}, Requested Amount = {self.amount}"


class SavingsAccount:
    # Constructor
    def __init__(self, no, name, balance=0):
        # Object attributes
        self.acno = no
        self.ahname = name
        # Private member
        self.__balance = balance

    # Methods
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise FundsError(self.__balance, amount)

    @property
    def balance(self):
        return self.__balance


a1 = SavingsAccount(1, "Steve")  # __init__ is called
a1.deposit(10000)
a1.deposit(5000)
a1.withdraw(20000)

print(a1.balance)
print(a1.__dict__)
# print(a1._SavingsAccount__balance)
