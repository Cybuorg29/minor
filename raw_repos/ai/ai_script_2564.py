def get_long_words(s):
    words = s.split(" ")
    result = []
    for word in words:
        if len(word) > 5:
            result.append(word)
    return result