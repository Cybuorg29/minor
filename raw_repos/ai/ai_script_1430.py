def ascii_to_decimal(string):
    decimal_value = 0
    for c in string:
        decimal_value += ord(c)
    return decimal_value

print(ascii_to_decimal('hello')) # Output -> 104 101 108 108 111