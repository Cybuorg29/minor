def two_sum(num, lst):
    indices = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == num:
                indices.append([i,j])
    return indices