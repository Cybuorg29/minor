import re

pattern = r'\b[a-zA-Z]*a[a-zA-Z]*z[a-zA-Z]*\b'

words = re.findall(pattern, "The quick brown fox jumped over the lazy dog")

for word in words:
    print(word)