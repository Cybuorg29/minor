def create_dict(list):
  return dict(zip(list, list))

dict = create_dict(list)
print(dict)
# Output: {'a': 'a', 'b': 'b', 'c': 'c'}