def get_alphabet_frequencies(sentence):
    """Function to generate a dictionary that contains the frequencies of all English alphabets in a given sentence"""
    alphabet_freq = dict()
    for el in sentence:
        if el.isalpha():
            el = el.lower()
            if el in alphabet_freq:
                alphabet_freq[el] += 1
            else:
                alphabet_freq[el] = 1
    return alphabet_freq

if __name__ == '__main__':
    sentence = "The brain is a powerful tool"
    alphabet_freq = get_alphabet_frequencies(sentence)
    print(alphabet_freq)