import re

def remove_non_alphabetic(string):
  return re.sub("[^a-zA-Z ]", "", string)