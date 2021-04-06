# Usage: python search_python_files.py searchstring [stardir]
import sys
import os


def file_contains(filename, st):
    try:
        with open(filename, "rt") as f:
            for line in f.readlines():
                if line.find(st) >= 0:
                    return True

            return False
    except:
        return False


if len(sys.argv) < 2:
    print("Usage: python search_python_files.py searchstring [startdir]")
    sys.exit()

if len(sys.argv) == 3:
    startdir = sys.argv[2]
else:
    startdir = "."  # Current directory

allfiles = os.walk(startdir)

for dirname, folders, files in allfiles:
    for file in files:
        filename = dirname + "\\" + file
        if filename.endswith(".py"):
            if file_contains(filename, sys.argv[1]):
                print(filename)
