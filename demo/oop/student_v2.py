class Student:
    courses = {'Python': 10000, 'DS': 20000, 'Java' : 15000}

    @staticmethod
    def get_course_fee(course):
        return Student.courses.get(course, None)

    def __init__(self, name, course="Python", feepaid=0):
        if not course in Student.courses:
            raise ValueError("Invalid Course")

        self.name = name
        self.course = course
        self.feepaid = feepaid

    def payment(self, amount):
        self.feepaid += amount

    def totalfee(self):
        return Student.courses[self.course]

    @property
    def balance(self):
        return self.totalfee() - self.feepaid


s = Student("Mike", "Python")
s.payment(5000)
print(s.totalfee())
print(s.balance)

print(Student.get_course_fee('Python'))
print(Student.get_course_fee('Java'))