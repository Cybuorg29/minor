def rot13(message):
    output = []
    for char in message:
        char_code = ord(char)
        if char_code >= ord('A') and char_code <= ord('Z'):
            # Rotate lower case characters
            char_code += 13
            if char_code > ord('Z'):
                char_code -= 26
        elif char_code >= ord('a') and char_code <= ord('z'):
            # Rotate upper case characters
            char_code += 13
            if char_code > ord('z'):
                char_code -= 26
        output.append(chr(char_code))
    return ''.join(output)
print(rot13("Hello World"))