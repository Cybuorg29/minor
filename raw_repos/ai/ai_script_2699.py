def calc_fibonacci_number(index):
    if index == 0 or index == 1:
        return index
    first_num = 0
    second_num = 1
    for i in range(2, index+1):
        next_num = first_num + second_num
        first_num, second_num = second_num, next_num
    return second_num