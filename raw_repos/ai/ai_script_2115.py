def calculate_std_dev(nums):
    mean = sum(nums)/len(nums)
    sum_deviation = 0
    for num in nums:
        diff = num - mean
        squared_deviation = diff ** 2
        sum_deviation += squared_deviation
    std_dev = (sum_deviation/(len(nums)-1)) ** 0.5
    return std_dev