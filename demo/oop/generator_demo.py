# Generator
def numbers():
    for n in range(1, 11):
        yield n


n = numbers()
print(type(n))

print(next(n))
print(next(n))
