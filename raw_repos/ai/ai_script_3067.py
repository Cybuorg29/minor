def merge_sort(arr):
    if len(arr) > 1: 
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        #calling merge sort function on left and right arrays
        merge_sort(L) 
        merge_sort(R) 

        i = j = k = 0
        # Copying data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
  
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

ar =[7,9,3,8,1]
merge_sort(ar)

# printing sorted array 
print (ar)