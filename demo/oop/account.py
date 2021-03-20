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
        self.__balance -= amount


a1 = SavingsAccount(1, "Steve")  # __init__ is called
a1.deposit(10000)
a1.deposit(5000)
print(a1.__dict__)
print(a1._SavingsAccount__balance)

