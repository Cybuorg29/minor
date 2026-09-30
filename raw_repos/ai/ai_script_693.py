def all_unique(string): 
  # loops through each character in string 
  for char in string: 
  
    # if character appears more than once, 
    # return False 
    if string.count(char) > 1: 
      return False 
      
  # return True if no characters appear more than once
  return True