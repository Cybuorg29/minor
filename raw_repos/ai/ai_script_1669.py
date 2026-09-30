def spell_checker(input_text):
    correct_words = []
    wrong_words = []
    
    for word in input_text.split():
        if is_correct(word):
            correct_words.append(word)
        else:
            wrong_words.append(word)
            
    return correct_words, wrong_words

# where is_correct() is an appropriate function to determine if the word is spelled correctly or not