import sys

# Add new folder to module search path - sys.path
sys.path.append(r"..\mylib")  # Raw string
print(sys.path)
import string_funs as sf


print(sf.hasupper('abc'))



