
def outer():
    v = 100
    def inner():
        nonlocal v
        v = v + 1
        print(v)

    inner()
    print(v)

outer()


