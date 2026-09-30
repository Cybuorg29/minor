def get_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for letter in str:
        if letter.lower() in vowels:
            res.append(letter)
    return res