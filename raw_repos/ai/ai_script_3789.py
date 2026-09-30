def find_median(arr):
    arr.sort()
    if len(arr) % 2 == 0: 
        median = (arr[(len(arr)//2)-1] + arr[len(arr)//2])/2 
    else: 
        median = arr[len(arr)//2] 
    return median

median = find_median([3,7,2,1,9])
print(median) # Prints 3.5