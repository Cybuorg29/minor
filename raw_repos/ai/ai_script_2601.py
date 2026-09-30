def isAnagram(string1, string2): 
    # get lengths of strings 
    string1_length = len(string1) 
    string2_length = len(string2) 
  
    # if length dont match
    if string1_length != string2_length: 
        return False
  
    # sorting both strings
    string1 = sorted(string1) 
    string2 = sorted(string2) 
  
    # compare the sorted strings 
    for i in range(0, string1_length): 
        if string1[i] != string2[i]: 
            return False
  
    return True

# testing
string1 = 'listen'
string2 = 'silent'
print(isAnagram(string1, string2)) # Output: True