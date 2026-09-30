def get_keys_by_value(my_dict, value):
  keys = []
  for k, v in my_dict.items():
    if v == value:
      keys.append(k)

  return keys

# Testing
my_dict = {'a': 1, 'b': 2, 'c': 2}
keys = get_keys_by_value(my_dict, 2)
print("Keys with the value 2 are: ", keys)