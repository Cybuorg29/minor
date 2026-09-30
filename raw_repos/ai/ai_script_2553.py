def string_to_int(s):
    res = 0
    for char in s:
        res = res * 10 + int(char)
    return res