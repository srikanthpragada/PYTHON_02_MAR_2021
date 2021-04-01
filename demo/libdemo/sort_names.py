# Take names from names.txt and display them in sorted order

f = open("names.txt","rt")
for n in sorted(map(str.strip,f.readlines())):
    print(n)

f.close()
