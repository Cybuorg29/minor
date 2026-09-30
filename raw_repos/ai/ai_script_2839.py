import re

pattern = re.compile(r'\bcomputer\b')

text = "A computer is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming."

matches = pattern.finditer(text)

for match in matches:
    print(match)