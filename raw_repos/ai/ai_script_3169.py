def replace_char(string, char_old, char_new):
    new_string = ''
    for char in string:
        if char == char_old:
            new_string = new_string + char_new
        else:
            new_string = new_string + char
    return new_string