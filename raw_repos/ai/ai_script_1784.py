def longest_word(sentence):
 longest_word = ""
 words = sentence.split()
 for word in words:
 if len(word) > len(longest_word):
 longest_word = word
 return longest_word