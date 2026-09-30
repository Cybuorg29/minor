import re
text = '\thello \tworld \t'
text = re.sub('\t', '    ', text)
print(text)