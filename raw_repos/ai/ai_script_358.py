def count_word(words, target_word):
    counter = 0
    for word in words:
        if word == target_word:
            counter += 1
    return counter