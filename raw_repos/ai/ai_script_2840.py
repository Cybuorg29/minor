def remove_duplicates(s):
  seen = []
  res = ""
  for char in s:
    if(char in seen):
      continue
    else:
      seen.append(char)
      res += char
  return res

string = 'Keeep Learning'
print(remove_duplicates(string)) # Keep Larning