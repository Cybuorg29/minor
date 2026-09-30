def is_alphabetical(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in phrase:
            return False
    return True