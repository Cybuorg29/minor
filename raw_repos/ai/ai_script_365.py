def has_special_characters(s):
    return not all(char.isalnum() for char in s)