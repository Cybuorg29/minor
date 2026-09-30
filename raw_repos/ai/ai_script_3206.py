def insert(arr, num): 
    # start from the rightmost element
    i = len(arr) - 1
    while ( i >= 0 and arr[i] > num):
        arr[i+1] = arr[i]
        i -= 1
  
    arr[i+1] = num