def is_ascending_order(nums):
    if len(nums) == 0 or len(nums) == 1:
        return True
    if nums[0] < nums[1]:
        return is_ascending_order(nums[1:])
    return False