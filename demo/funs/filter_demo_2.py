names = ['abc', 'xyz12', '12', 'pqr', 'def']


# Using filter
def hasdigit(s : str) -> bool:
    for c in s:
        if c.isdigit():
            return True

    return False


for n in filter(hasdigit, names):
    print(n)
