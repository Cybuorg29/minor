def compare_arrays(arr1, arr2, arr3):
  common_elements = []
  for elem in arr1:
    if elem in arr2 and elem in arr3:
      common_elements.append(elem)
  print(common_elements)