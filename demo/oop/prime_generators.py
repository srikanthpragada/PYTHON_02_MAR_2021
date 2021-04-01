# Generator to generate prime numbers between given range
def primes(start, end):
    for n in range(start, end + 1):
        for i in range(2, n//2 + 1):
            if n % i == 0:
                break
        else:
            yield n


g = primes(100,200)
for v in g:
    print(v)
