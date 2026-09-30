import re

def check_digits(string):
  """
  This function takes a string and
  checks if it contains any digit.
  """
  regex_pattern = r"[0-9]" 
  return bool(re.search(regex_pattern, string))