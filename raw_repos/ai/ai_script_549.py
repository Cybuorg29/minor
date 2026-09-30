def max_m_consecutive_sum(arr, m):
    max_sum = 0
    for i in range(len(arr) - m + 1):
        curr_sum = 0
        for j in range(i, i + m):
            curr_sum += arr[j]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum