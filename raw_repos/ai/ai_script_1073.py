def find_pair(arr,k):
  pairs = []
  found_elements = set()
  for num in arr:
    diff = k - num
    if diff in found_elements:
      pairs.append([min(num,diff), max(num,diff)])
    found_elements.add(num)
  return pairs