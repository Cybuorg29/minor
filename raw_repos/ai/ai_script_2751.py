import re
value = 'The integer value is 12'
 
m = re.search(r'\d+', value)
print(int(m.group(0)))