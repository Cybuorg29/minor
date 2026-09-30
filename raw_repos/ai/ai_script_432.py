import re
 
prefix = "ABC"
pattern = re.compile('^' + prefix + '\d{2,}[A-Za-z]{2,}$')