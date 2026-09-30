def replaceSubstring(string, substring1, substring2): 
    string = string.replace(substring1, substring2) 
    return string  
  
# Driver code
string = "I am coding in python"
substring1 = "coding"
substring2 = "hacking"
print("String after replacement is:", replaceSubstring(string, substring1, substring2))