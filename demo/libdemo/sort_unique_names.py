# Take names from allnames.txt and sort unique names

f = open("allnames.txt","rt")
names = set()
for line in f.readlines():
    for name in line.split(','):
        name = name.strip()
        if len(name) > 0:
            names.add(name)

for name in sorted(names):
    print(name)

f.close()