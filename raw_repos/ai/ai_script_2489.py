def RunLengthEncoding(string):
    result = "" 
    count = 0
    current = string[0] 
  
    for i in range(len(string)): 
        if (string[i] == current): 
            count+= 1 
        else: 
            result += current + str(count) 
            current = string[i] 
            count = 1
    result += current + str(count)
  
    return result