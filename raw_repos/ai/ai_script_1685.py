def count_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count

count_vowels(sentence)