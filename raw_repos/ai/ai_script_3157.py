def checkDigits(string):
    for char in string:
        if char not in '1234567890':
            return False
    return True

print(checkDigits('12345'))

OUTPUT:
True