class SavingsAccount:
    # Constructor
    def __init__(self, no, name, balance=0):
        # Object attributes
        self.acno = no
        self.ahname = name
        self.balance = balance

        # Methods

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


a1 = SavingsAccount(1, "Steve")  # __init__ is called
a1.deposit(10000)
a1.deposit(5000)
print(a1.balance)

a2 = SavingsAccount(2, "Tom", 50000)
print(a2.balance)
