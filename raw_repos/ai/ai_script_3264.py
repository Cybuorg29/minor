import re

# The given string
my_string = 'Hi There! Welcome.@'

# Remove special characters using regular expressions
clean_string = re.sub('[^a-zA-Z0-9\s]', '', my_string)
print(clean_string) # Hi There Welcome