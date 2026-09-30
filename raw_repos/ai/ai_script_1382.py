def findMin(arr):
    current_min = arr[0]
    for num in arr:
        if num < current_min:
            current_min = num
    return current_min