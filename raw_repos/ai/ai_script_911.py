def sum_of_square_range(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i * i
    return sum