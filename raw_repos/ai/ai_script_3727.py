def larger_num(myList): 
    
    # Initialize maximum element 
    max = myList[0] 
  
    # Traverse list elements from second and 
    # compare every element with current max  
    for i in range(1, len(myList)): 
        if myList[i] > max: 
            max = myList[i] 
    return max 
  
myList = [18, 24, 34, 30]
print(larger_num(myList))