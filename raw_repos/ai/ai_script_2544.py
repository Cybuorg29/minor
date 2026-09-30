def longest(words): 
    max_len = 0
    
    for i in range(0, len(words)): 
        if (len(words[i]) > max_len): 
            max_len = len(words[i])
            longest = words[i] 
  
    return longest