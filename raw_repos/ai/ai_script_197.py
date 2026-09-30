def has_unique_chars(string): 
  chars = set() 
  for char in string: 
    if char in chars: 
      return False 
    else: 
      chars.add(char) 
  return True