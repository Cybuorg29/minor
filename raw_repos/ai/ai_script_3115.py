def count_chars(string):
    if len(string) == 0:
        return 0
    return 1 + count_chars(string[1:])