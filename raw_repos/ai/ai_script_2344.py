def find_missing(nums):
    count = 1
    for num in nums:
        if not count in nums:
            return count
        count += 1
    return None