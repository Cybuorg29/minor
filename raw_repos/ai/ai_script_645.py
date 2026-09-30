def countChar(string, char):
  ctr = 0
  for s in string:
    if s == char:
      ctr += 1
  return ctr