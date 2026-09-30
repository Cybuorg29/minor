def merge_sort(arr): 
    # Base case: if the list has 0 or 1 elements it is already sorted 
    if len(arr) > 1: 
        mid = len(arr)//2 
        # Split the array 
        left = arr[:mid]  
        right = arr[mid:]  
  
        # Recursively call merge_sort on left and right half
        merge_sort(left) 
        merge_sort(right) 
  
        # Set up variables to help track merges
        i = 0 # left array index 
        j = 0 # right array index 
        k = 0 # result array index 
  
        # Merge the two halves 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1 
            else: 
                arr[k] = right[j] 
                j+=1 
            k+=1
          
        # Copy the rest of the left half and right half 
        while i < len(left): 
            arr[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1