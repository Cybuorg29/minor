def find_pair(numbers, target):
  nums_set = set(numbers)
  for num in nums_set:
    if target - num in nums_set:
      return [num, target-num]