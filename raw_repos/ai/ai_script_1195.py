def character_frequency(word):
    freq_dict = {}
    for char in word:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

word = 'Python'
print(character_frequency(word))
# {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}