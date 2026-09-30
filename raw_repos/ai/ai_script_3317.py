def find_word(word, text):
    # Use the 'in' operator to check if the word is in the text
    if word in text:
        return "Word found"
    else:
        return "Word not found"

# Use the 'count' method to check if the word is in the text more efficiently
if text.count(word) > 0:
    return "Word found"
else:
    return "Word not found"