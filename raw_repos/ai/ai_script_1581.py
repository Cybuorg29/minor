def max_pairwise_product(nums):
  max_product = 0
  for i in range(len(nums)):
      for j in range(i+1,len(nums)):
          max_product = max(max_product, nums[i] * nums[j])
  return max_product