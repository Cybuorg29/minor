def flatten_2d_list(lst):
  flat_list = []
  for elem in lst:
    for item in elem:
      flat_list.append(item)
  return flat_list

test_list = [[1,2], [3,4], [5,6]] 
print(flatten_2d_list(test_list))