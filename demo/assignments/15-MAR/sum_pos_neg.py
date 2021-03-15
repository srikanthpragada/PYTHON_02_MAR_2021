def sum_pos_neg(*nums):
    pos_sum = neg_sum = 0
    for n in nums:
        if n > 0:
            pos_sum += n
        else:
            neg_sum += n

    return (pos_sum, neg_sum)  # return a tuple


print(sum_pos_neg(10, 20, -10, -5, -25, 30))
