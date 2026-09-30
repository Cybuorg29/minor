def find_smallest_number(arr):
    """
    Finds the smallest number in an array of numbers.
    """
    min_num = arr[0]
    for num in arr[1:]:
        if num < min_num:
            min_num = num
    return min_num