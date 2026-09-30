def replace_word(sentence, word, replacement):
    words = sentence.split(" ")
    new_sentence = ""
    for w in words:
        if w == word:
            w = replacement
        new_sentence += w + " "
    return new_sentence

sentence = "I like apples"
word = "apples"
replacement = "bananas"

print(replace_word(sentence, word, replacement))