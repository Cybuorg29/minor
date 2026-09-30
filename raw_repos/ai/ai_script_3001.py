def pig_latin(text):
    words = text.split()
    Latin_words = []
    # loop through every word 
    for word in words:
        # seperate consonants from vowels
        firstletter = word[0]
        if firstletter.lower() in 'aeiou':
            Latin_word = word+'ay'
        else:
            Latin_word = word[1:]+firstletter+'ay'
        Latin_words.append(Latin_word)
    return " ".join(Latin_words)