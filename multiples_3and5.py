def sum_multiples_3or5(num):
    sum_num = 0
    for i in range(1, num):
        if i % 3 == 0:
            sum_num += i
        elif i % 5 == 0:
            sum_num += i
    return sum_num


print sum_multiples_3or5(10)
