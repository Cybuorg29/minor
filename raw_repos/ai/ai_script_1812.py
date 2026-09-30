def is_valid_number(string):
    for c in string:
        if not c.isdigit():
            return False
    return True

print(is_valid_number('abc123')) # Output -> False