def is_anagram(word1, word2):
    word1 = word1.upper()
    word2 = word2.upper()
    return sorted(word1) == sorted(word2)