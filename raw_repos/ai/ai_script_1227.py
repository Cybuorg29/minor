def min_index(list):
    min_val = list[0]
    min_index = 0
    for i, val in enumerate(list):
        if val < min_val:
            min_val = val
            min_index = i
    return min_index