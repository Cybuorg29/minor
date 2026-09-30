def removeInts(arr): 
    return [x for x in arr if type(x) is not int] 

print(removeInts(["Hello", 3, 5.4, "World", 6])) 

# output
['Hello', 5.4, 'World']