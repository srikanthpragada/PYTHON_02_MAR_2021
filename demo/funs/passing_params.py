def zero(n):
    print(id(n))
    n = 0
    print(id(n))


def prepend(lst,num):
    lst.insert(0,num)

a = 10
print(id(a))
zero(a)
print(a)

l = [1,2,3]
prepend(l,10)
print(l)
