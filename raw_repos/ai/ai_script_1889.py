import re

def replace_non_alphanum(string, character):
    return re.sub(r'\W', character, string)

string = 'Hello, world!'
character = '#'

print(replace_non_alphanum(string, character))