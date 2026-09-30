def unique_chars(string):
    # List to keep track of characters 
    characters = []
    
    for c in string:
        if c not in characters:
            characters.append(c)
        else:  
            return False
    
    return True