def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(count_words("the quick brown fox jumps over the lazy dog"))
# Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}