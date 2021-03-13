# positional-only arguments
def area(w, l, /):
    return l * w


print(area(10,20))
# print(area(width=20, length=10))
