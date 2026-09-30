def maximize_sum(arr, k):
    arr.sort()
    result = 0
    for i in range(len(arr)-1, len(arr)-k-1, -1):
        result += arr[i]
    return result