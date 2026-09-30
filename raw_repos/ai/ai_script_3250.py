def printAllKeys(dictionary): 
    if type(dictionary) == dict: 
        for key in dictionary: 
            print(key) 
            printAllKeys(dictionary[key])