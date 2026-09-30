def combine_lists(list1,list2):
  result = []
  for i in list1:
    for j in list2:
      result.append([i,j])
  return result