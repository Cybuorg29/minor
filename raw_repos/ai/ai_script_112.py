def extract_words(str): 
    
    # to store the extracted words 
    words = [] 
  
    # split the string 
    word = "" 
    for i in str: 
        if i is not " ": 
            word = word + i 
        else: 
            words.append(word) 
            word = ""             
    words.append(word) 
      
    # return the list of words 
    return words  
  
# Driver code 
str = "Welcome to the world of Geeks"
words = extract_words(str) 
for i in words: 
    print(i)