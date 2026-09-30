def remove_letter(string, letter):
    output = ""
    for s in string:
        if s != letter:
            output += s
    return output