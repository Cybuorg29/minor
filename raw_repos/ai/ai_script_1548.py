def remove_special_characters(string): 
    final_string = "" 
    for character in string: 
        if character.isalnum(): 
            final_string += character 
    return final_string