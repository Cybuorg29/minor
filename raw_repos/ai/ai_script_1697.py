def most_frequent(nums):
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    max_count = 0
    res = 0
    for key, val in count.items():
        if val > max_count:
            res = key
        max_count = max(max_count, val)
    return res