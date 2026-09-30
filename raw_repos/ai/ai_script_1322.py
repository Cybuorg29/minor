def remove_non_alphanumeric(string):
    filtered_string = ""
    for char in string:
        if char.isalnum():
            filtered_string += char
    return filtered_string