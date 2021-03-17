def even_odd(n):
    if n % 2 == 0:
        return 0
    else:
        return 1


nums = [10, 11, 20, 15, 35, 40, 80]

for n in sorted(nums, key=even_odd):
    print(n)
