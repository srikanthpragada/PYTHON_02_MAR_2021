# Take names from names.txt and display them in sorted order

with open("names.txt","rt") as f:
    for n in sorted(map(str.strip,f.readlines())):
        print(n)

