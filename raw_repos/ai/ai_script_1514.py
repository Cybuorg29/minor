def find_substring(main_string, substring):
  indices = []
  position = -1
  while True:
    position = main_string.find(substring, position + 1)
    if position == -1:
      break
    indices.append(position)
  return indices