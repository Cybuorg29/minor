def array_sum(arr):
    sum = 0
    for i in range(0, len(arr)-1, 2):
        sum += arr[i] + arr[i+1]
    return sum