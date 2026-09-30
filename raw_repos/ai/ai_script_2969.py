import re
pattern = r"\b\w{7,}\b"

sentence = "This is a sample sentence to test"
matches = re.findall(pattern, sentence)
 
print(matches)