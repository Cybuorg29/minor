def frequencySort(arr): 
    eleFreq = {} 
    sortedList = [] 
  
    # Create a dictionary with frequency of element as key and element as value
    for i in arr: 
        if i in eleFreq: 
            eleFreq[i] += 1
        else: 
            eleFreq[i] = 1
  
    # Sort the dictionary 
    sortedFreq = sorted(eleFreq.items(), key = lambda eleFreq: eleFreq[1], reverse = True) 
  
    # Store the elements in an output list with the same frequency 
    for i in sortedFreq: 
        sortedList.extend([i[0]] * i[1])
  
    return sortedList