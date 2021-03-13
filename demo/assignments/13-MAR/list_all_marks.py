data = [(1, 50), (1, 60), (2, 55), (2, 70), (4, 70), (3, 90), (4, 60)]

students = {}
for rollno, marks in data:
    if rollno in students:  # Existing student
        students[rollno].append(marks)
    else:
        students[rollno] = [marks]  # Add new student

for rollno, marks in sorted(students.items()):
    smarks = [str(m) for m in marks]
    print(f"{rollno:5} {sum(marks):5} {','.join(smarks)}")

