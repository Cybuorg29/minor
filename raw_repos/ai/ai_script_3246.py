def isAnagram(str1, str2): 

 # convert both strings into lowercase 
 str1 = str1.lower()
 str2 = str2.lower()
  
 # sort both strings 
 sortedStr1 = ''.join(sorted(str1)) 
 sortedStr2 = ''.join(sorted(str2)) 
  
 # check if sorted strings are equal 
 if sortedStr1 == sortedStr2: 
     return True
 else: 
     return False

result = isAnagram(string1, string2)
print(result)