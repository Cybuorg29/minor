def search(nums, x):
    for i, n in enumerate(nums):
        if n == x:
            return i
    return -1