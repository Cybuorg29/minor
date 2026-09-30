def count_capital_letters(string_list):
  count = 0
  for string in string_list:
    for char in string:
      if char.isupper():
        count += 1
  return count