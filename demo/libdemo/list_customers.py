import re

f = open("customers.txt","rt")
customers = {}

for line in f.readlines():
    # Look for name
    name_match = re.search('[A-Za-z ]+',line)
    if name_match is None:
        continue
    name = name_match.group(0).strip()
    # Look for mobile
    mobile_match = re.search(r'\d+', line)
    if mobile_match is None:
        continue
    mobile = mobile_match.group(0)
    customers[name] = mobile

f.close()

for name,mobile in sorted(customers.items()):
    print(f"{name:20} {mobile}")

