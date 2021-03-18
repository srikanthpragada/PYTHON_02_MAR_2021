# Number functions

def iseven(n):
    """
    Returns true if the given number is even otherwise false

    Usage : iseven(n)
    Parameter n is the number to test
    """
    return n % 2 == 0


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


# WHen you run module as script, do this
if __name__ == '__main__':
    print("number_funs module!")
