def count_unique_chars(s):
    chars = set()
    for char in s:
        chars.add(char)
    return len(chars)