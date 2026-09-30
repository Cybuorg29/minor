def print_indices(x, arr):
    indices = []
    for i in range(len(arr)):
        if arr[i] == x:
            indices.append(i)
    return indices

print(print_indices(x, arr))  # [1, 4]