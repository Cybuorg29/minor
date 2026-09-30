def reverse_string(string): 
  # Create an empty string 
  rev_string = "" 
  
  # Iterate through the string and build the reversed string 
  for char in string: 
    rev_string = char + rev_string 
  
  # Return the reversed string 
  return rev_string 

print(reverse_string(string)) # dlrow olleH