def is_anagram(str1, str2): 
    # convert the strings to lowercase 
    str1 = str1.lower() 
    str2 = str2.lower() 

    # sorting both the strings 
    s1 = sorted(str1) 
    s2 = sorted(str2) 

    if len(s1) != len(s2): 
        return False

    # compare character by character 
    for i in range(len(s1)): 
        if s1[i] != s2[i]: 
            return False
    return True

# Driver code 
if is_anagram("spite", "pists"):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")