def is_permutation(str1, str2): 
    """
    Function to check if the given string str1 is a permutation of the string str2 
    
    Parameters: 
    str1 (str): first string 
    str2 (str): second string 
    
    Returns: 
    bool: True if str1 is a permutation of str2, False otherwise
    """
    if (len(str1) != len(str2)): 
        return False
    else: 
        count = [0] * 128
        for i in range(len(str1)):
            count[ord(str1[i])] +=1
            count[ord(str2[i])] -=1
        for i in range(128):
            if count[i] != 0: 
                return False
        return True