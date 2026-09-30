def find_max_product(nums):
  max_product = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      product = nums[i] * nums[j]
      if product > max_product:
        max_product = product
  return max_product