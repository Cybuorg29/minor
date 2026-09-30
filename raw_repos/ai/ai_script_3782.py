import re

sentence = "I I am going to the the store"
result = re.sub(r'\b(\w+)( \1\b)+', r'\1', sentence)
print(result) # I am going to the store