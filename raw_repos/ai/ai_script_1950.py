def count_occurrences(string1, string2): 
    
    # Initialize count to 0
    count = 0
    
    # Iterate over the first string
    for i in range(len(string1)): 
        # Slice the element from i to length of second string
        temp = string1[i: i + len(string2)] 
  
        # If sliced string and second string are equal, 
        # increase count by one
        if temp == string2: 
            count+= 1
  
    return count