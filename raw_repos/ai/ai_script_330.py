def has_all_alphabet(string):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return set(letters).issubset(string.upper())