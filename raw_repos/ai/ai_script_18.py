def get_unique_words(input_string):
    words = input_string.split()
    unique_words = set(words)
    return list(unique_words) # Retruns a list of all unique words present in the string.