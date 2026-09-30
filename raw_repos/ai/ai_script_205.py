def selection_sort(list):
    # Traverse through all array elements 
    for i in range(len(list)): 
      
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(list)): 
            if list[min_idx] > list[j]: 
                min_idx = j 
          
        # Swap the found minimum element with  
        # the first element         
        list[i], list[min_idx] = list[min_idx], list[i] 
  
# Driver code to test above 
list = [3, 6, 8, 9, 5] 
selection_sort(list) 
print ("Sorted array") 
for i in range(len(list)): 
    print("%d" %list[i])