def max_num(arr):
    n = arr[0]
    for i in range(len(arr)):
        if arr[i] > n:
            n = arr[i]
    return n

max_num([2, 4, 8, 6]) # Output: 8