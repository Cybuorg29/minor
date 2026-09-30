import re 
  
def is_alphabetic(string):  
    Pattern = re.compile("^[a-zA-Z]*$")
    return bool(Pattern.match(string))