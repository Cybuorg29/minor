import string

def replace_punctuation(string):
    for char in string:
        if char in string.punctuation:
            string = string.replace(char, " ")
    return string