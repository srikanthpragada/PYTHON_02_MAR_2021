# Print dept no and list of employees from employees.txt
f = open("employees.txt", "rt")
depts = {}
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    deptno = parts[0]
    names = [n.strip() for n in parts[1:]]
    if deptno in depts:
        depts[deptno] = depts[deptno] | set(names)
    else:
        depts[deptno] = set(names)

f.close()
# Print
for deptno, names in sorted(depts.items()):
    print(f"{deptno:5} {','.join(sorted(names))}")
