def longest_element(list):
  max_length = 0
  max_length_item = None

  for item in list:
    if len(item) > max_length:
      max_length = len(item)
      max_length_item = item

  return max_length_item

list = [10, 100, 200, 500, 400]
longest_element(list) # 500