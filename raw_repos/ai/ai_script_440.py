def is_anagram(string1, string2):
    # Create a dictionaries for strings
    string1_dict = {}
    string2_dict = {}
  
    # Add the chars from each string to the dictionaries
    for char in string1:
        if char not in string1_dict:
            string1_dict[char] = 1
        else:
            string1_dict[char] += 1
    
    for char in string2:
        if char not in string2_dict:
            string2_dict[char] = 1
        else:
            string2_dict[char] += 1
    
    # Check if the dictionaries have the same entries
    for key in string1_dict:
        if key not in string2_dict:
            return False
        elif string1_dict[key] != string2_dict[key]:
            return False
    
    return True
  
# Test the algorithm
string1 = "listen"
string2 = "silent"

if(is_anagram(string1, string2)):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")