def even_length_words(word_list):
    even_words = []
    for word in word_list:
        if len(word) % 2 == 0:
            even_words.append(word)
    return even_words
    
if __name__ == '__main__':
    print(even_length_words(word_list))