data = [(1, 50), (1, 60), (2, 55), (2, 70), (4, 70), (3, 90), (4, 60)]

students = {}
for rollno, marks in data:
    if rollno in students:  # Existing student
        students[rollno] += marks
    else:
        students[rollno] = marks  # Add new student

for rollno, total in sorted(students.items()):
    print(f"{rollno:5} {total:4}")

print(students)
