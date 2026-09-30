# Print all unique combinations of an array of integers

def all_combinations(nums):
  result = [[]]
  for num in nums:
    temp_result = []
    for res in result:
      temp_result.append(res + [num])
    result.extend(temp_result)
  return result

print(all_combinations(nums)) # [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]