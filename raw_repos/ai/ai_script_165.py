def uniq_array(nums):
    distinct_arr = []
    for num in nums:
        if num not in distinct_arr:
            distinct_arr.append(num)
    return distinct_arr