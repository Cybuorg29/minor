def find_largest(nums):
    largest = nums[0]
    for num in nums[1:]:
        if num > largest:
            largest = num
    return largest