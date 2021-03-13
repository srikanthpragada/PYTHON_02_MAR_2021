# Keyword-only arguments
def area(*, width, length):
    return length * width


# area(10, 20)
print(area(length=10, width=20))
print(area(width=20, length=10))
