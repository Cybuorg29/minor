def findSumPairs(arr, target): 

    # X stores elements and its 
    # frequencies in a dictionary 
    X = dict() 
    n = len(arr) 
    output = [] 
  
    # Store counts of all elements 
    # of array in a hash 
    for i in range(0, n): 
        if arr[i] in X.keys(): 
            X[arr[i]] += 1
        else: 
            X[arr[i]] = 1

    # Loop over each element 
    for i in range(0, n): 
        # finding the compliment 
        k = target - arr[i] 

        # If compliment exists in X 
        # and it is not the same element 
        if (k in X.keys() and X[k] != 0
            and k != arr[i]): 
            output.append([arr[i], k]) 
            X[k] = X[k] - 1
  
    # return content of output 
    return output 

# calling the findSumPairs function 
print(findSumPairs(array, target)) 

# Output: [[1, 4], [2, 3]]