def max_subarray_sum(arr):
    max_sum = 0
    curr_sum = 0
    for x in arr:
        curr_sum += x
        if curr_sum < 0:
            curr_sum = 0
        elif curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_sum(arr))