def is_pangram(s):
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in s:
            return False
    return True