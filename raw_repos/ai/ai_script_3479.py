def filter_negative_numbers(nums):
    # return only positive numbers
    return [num for num in nums if num >= 0]

print(filter_negative_numbers([2, 3, -1, 4, -5, 6]))