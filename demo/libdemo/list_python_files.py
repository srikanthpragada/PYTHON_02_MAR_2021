import os

allfiles = os.walk(r"d:\classroom\mar2\demo")

for dirname, folders, files in allfiles:
    for file in files:
        if file.endswith(".py"):
            print(dirname + "\\" + file)
