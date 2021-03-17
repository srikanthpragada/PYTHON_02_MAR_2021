def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


names = ['Java', 'python', 'C', 'C++', 'TypeScript', 'JavaScript']

for l in map(count_upper, names):
    print(l)
