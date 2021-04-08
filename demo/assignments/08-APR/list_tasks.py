from datetime import datetime

formats = ["%d-%m-%Y", '%m-%d-%Y', '%Y-%m-%d']
today = datetime.now()
f = open("tasks.txt", "rt")
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    for format in formats:
        try:
            stdate = datetime.strptime(parts[1], format)
            td = today - stdate
            print(f"{parts[0]} - {td.days}")
            break
        except:
            pass

f.close()
