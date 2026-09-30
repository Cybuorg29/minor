def longest_substring(string): 
    n = len(string) 
  
    ''' Initialization of stings, 
    a and b ''' 
    a = "" 
    b = ""  
  
    ''' Initialization of maximum length substring 
    having distinct characters ''' 
    maxlen = 0  
  
    ''' 1. Pick starting point 
    2. intialise substrng "a"
    3. Find the longest such 
    substring by comparing 
    current and previous  
    substring ''' 
    for i in range(n):
        a += string[i] 
        b = "" 
        for j in range(i + 1, n): 
            if string[j] not in a:              
                b += string[j] 
            else: 
                break
        if len(a) > maxlen: 
            maxlen = len(a) 
        a += b
    return maxlen