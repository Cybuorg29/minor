def find_longest_word(lst):
    longest_word = ""
    for word in lst:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word