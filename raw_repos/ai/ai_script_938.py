def reverse_nums(num_list):
    n = len(num_list)
    for i in range(n//2):
        num_list[i], num_list[n-i-1] = num_list[n-i-1], num_list[i]
    return num_list