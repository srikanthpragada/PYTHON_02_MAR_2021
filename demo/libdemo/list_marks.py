# Print name and average marks for each student from marks.txt file
f = open("marks.txt","rt")

for line in f.readlines():
    parts = line.split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    marks = [int(m) for m in parts[1:] if m.isdigit()]
    total = sum(marks)

    if len(marks) < 1:
        avg = 0
    else:
        avg = total / len(marks)

    print(f"{name:20} {avg:5.2f}")


f.close()

