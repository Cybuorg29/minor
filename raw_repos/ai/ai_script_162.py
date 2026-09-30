def get_mean_median(nums):
    num_count = len(nums) 
    num_sum = 0.0
    for num in nums: 
        num_sum += num
  
    mean = num_sum / num_count 
  
    nums.sort() 
    if num_count % 2 == 0: 
        median1 = nums[num_count//2] 
        median2 = nums[num_count//2 - 1] 
        median = (median1 + median2)/2
    else: 
        median = nums[num_count//2] 
  
    return mean, median