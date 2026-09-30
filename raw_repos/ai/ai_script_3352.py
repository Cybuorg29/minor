def triplet_sum(nums, target):
 for i in range(len(nums) - 2):
  for j in range(i+1, len(nums) - 1):
   for k in range(j+1, len(nums)):
    if nums[i] + nums[j] + nums[k] == target:
     return True
 return False
 
print(triplet_sum(nums, target))