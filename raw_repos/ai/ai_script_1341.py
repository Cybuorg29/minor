def largest_sum_of_consecutive_ints(arr):
    largest_sum = 0
    for i in range(len(arr)):
        if i < len(arr)-1:
            current_sum = arr[i] + arr[i+1]
            largest_sum = max(largest_sum, current_sum)
    return largest_sum