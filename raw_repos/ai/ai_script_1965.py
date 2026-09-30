def delete_char(string, character):
    new_string = ""
    for char in string:
        if char != character:
            new_string += char
    return new_string