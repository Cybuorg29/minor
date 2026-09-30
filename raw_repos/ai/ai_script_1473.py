def jumbledLetters(word):
    """Returns a randomly jumbled version of the given word."""
    new_word = ""
    for letter in word:
        #__TODO__ use the random module to generate a number between 0 and the length of the word
        num = random.randint(0, len(word)-1)
        #__TODO__ add the letter to the string `new_word` using the `num` generated in the previous step
        new_word += word[num]
    return new_word