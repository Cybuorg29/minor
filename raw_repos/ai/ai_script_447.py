def max_subarray_sum(arr):
    max_sum = 0
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum