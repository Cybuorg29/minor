def find_index_max(arr):
    max_index = 0
    for i in range(1, len(arr)):
        if arr[max_index] < arr[i]:
            max_index = i
    return max_index