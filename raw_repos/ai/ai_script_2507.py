def isAnagram(s1, s2): 
  
    # Get lengths of both strings 
    n1 = len(s1) 
    n2 = len(s2) 
  
    # If lengths of both strings are not same, then they are not anagram 
    if n1 != n2: 
        return False
  
    # Sort both strings 
    s1 = sorted(s1) 
    s2 = sorted(s2) 
  
    # Compare sorted strings 
    for i in range(0, n1): 
        if s1[i] != s2[i]: 
            return False
  
    return True

# driver code
s1 = "listen"
s2 = "silent"
print("The two strings are anagrams:", isAnagram(s1, s2))