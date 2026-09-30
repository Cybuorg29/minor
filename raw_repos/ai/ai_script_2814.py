def reverse_words(string):
    words = string.split(' ')
    reversed_words = ' '.join(words[::-1])
    return reversed_words