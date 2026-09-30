def firstIndex(str, char): 
    index = -1
    for i in range(len(str)):  
        if (str[i] == char):  
            index = i 
            break
    return index 

result = firstIndex(str, char) 
print(result) # prints 4