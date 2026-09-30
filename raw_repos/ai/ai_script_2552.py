def unique_chars(string): 
    char_list = [] 
    for char in string: 
        if(char not in char_list): 
            char_list.append(char) 
    return char_list