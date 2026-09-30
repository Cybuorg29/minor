def removeCharFromString(string, char):
  result_string = []
  for c in string:
    if c != char:
      result_string.append(c)
  return ''.join(result_string)