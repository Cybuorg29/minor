def filter_length(arr, th):
  subset = []
  for el in arr:
    if len(el) <= th:
      subset.append(el)
  return subset