class Student:
    def __init__(self, name, course="Python", feepaid=0):
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def payment(self, amount):
        self.feepaid += amount

    def totalfee(self):
        return 10000 if self.course == "Python" else 20000

    def getbalance(self):
        return self.totalfee() - self.feepaid


s = Student("Mike", "DS")
s.payment(10000)
print(s.totalfee())
print(s.getbalance())

