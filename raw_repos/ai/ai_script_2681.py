def minAbsDifference(arr):
    min_difference = float("inf")
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff < min_difference:
                min_difference = diff
    return min_difference