def longest_string(list):
  longest_word = ""
  for word in list:
    if len(word) > len(longest_word):
      longest_word = word
  return longest_word