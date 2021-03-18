import sys

if len(sys.argv) < 2:
    print("Usage : python table.py number [length]")
    exit(0)   # stop program

num = int(sys.argv[1])  # Second parameter
if len(sys.argv) > 2:
    length = int(sys.argv[2])
else:
    length = 10

for n in range(1, length + 1):
    print(f"{num:4}  * {n:2} = {n * num:6}")
