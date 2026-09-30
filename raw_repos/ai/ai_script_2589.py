def contains_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string.lower():
        if char in vowels:
            return True
    return False