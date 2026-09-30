def replace_char_at(str, index, new_char):
    """This function takes in a string and a number and returns a new string with the character at the given index replaced with another character."""
    return str[:index] + new_char + str[index + 1:]