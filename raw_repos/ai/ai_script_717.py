def get_average_sum(arr):
    total = 0
    count = 0
    for sub_arr in arr:
        total += sum(sub_arr)
        count += len(sub_arr)
    return total / count