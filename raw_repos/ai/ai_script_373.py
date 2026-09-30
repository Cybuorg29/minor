def replace_kth_smallest(nums, k):
    min_num = min(nums)
    min_count = nums.count(min_num)
    if k > min_count:
        k -= min_count
        nums.remove(min_num)
    nums[k-1] = 0
    return nums