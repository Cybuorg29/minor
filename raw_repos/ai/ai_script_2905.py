def closest_number(nums, number): 
  min_diff = abs(nums[0] - number) 
  min_num = nums[0] 
  for num in nums:
    min_diff_temp = abs(num - number) 
    if min_diff_temp < min_diff:
    	min_diff = min_diff_temp
    	min_num = num
  return min_num