nums = [10, -10, 9, 8, -5, 30]

pos_nums = []
for n in nums:
    if n > 0:
        pos_nums.append(n)

print(pos_nums)


# Using filter
def ispositive(n):
    return n > 0


for n in filter(ispositive, nums):
    print(n)
