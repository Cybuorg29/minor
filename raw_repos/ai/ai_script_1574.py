def filter_3(nums):
    result = []
    for num in nums:
        if num % 3 != 0:
            result.append(num)
    return result