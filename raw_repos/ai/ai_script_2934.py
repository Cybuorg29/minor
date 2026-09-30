def toInt(string):
    number = 0
    for char in string:
        number = (number * 10) + int(char)
    return number

# Test
print(toInt(string)) #12345