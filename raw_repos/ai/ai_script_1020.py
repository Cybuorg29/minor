def classify_word(word):
    """
    This function takes a word as a parameter and returns its classification - verb or noun.
    """
    if word in ["run", "jump", "swim"]:
        return "verb"
    else: 
        return "noun"

print(classify_word("write")) # prints "verb"