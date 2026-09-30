def most_occurrences(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1

    freq_words = [(freq[word], word) for word in freq]
    freq_words.sort(reverse=True)
    print(freq_words[:2])

most_occurrences("This is just a simple string")