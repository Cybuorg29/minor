def count_occurrences(string, character): 
  count = 0
  for i in range(len(string)):
    if string[i] == character:
      count += 1
  return count