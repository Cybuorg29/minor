def remove_duplicates_from_sentence(sentence): 
    split_words = sentence.split(' ')
    no_duplicates = list(set(split_words))
    return ' '.join(no_duplicates)