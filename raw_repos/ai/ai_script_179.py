def alphabetically_sort_words(str):
    words = str.split(' ')
    words.sort()
    return words

print(alphabetically_sort_words("Here is a sentence to sort")) # prints ['Here', 'a', 'is', 'sentence', 'sort', 'to']