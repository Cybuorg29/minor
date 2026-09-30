def shift_string(string):
  result = ""
  for ch in string:
    result += chr(ord(ch) + 1)
  return result