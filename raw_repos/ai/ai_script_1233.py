import re

string = "This is a programming task"

pattern = r"is"

if re.search(pattern, string):
  print("Match found")
else:
  print("No match found")