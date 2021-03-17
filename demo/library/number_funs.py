# Number functions

def iseven(n):
    return n % 2 == 0


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0
