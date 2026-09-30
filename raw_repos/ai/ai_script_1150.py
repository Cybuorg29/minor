def longest_word(sentence):
    words = sentence.split()
    max_len = len(words[0])
     
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            max_word = word
     
    return max_word
 
print(longest_word('I am Python Programmer'))

Output: Programmer