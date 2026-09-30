A simple approach to reverse an array is to use two index variables, one at the start and one at the end of the array. Swap the elements present at these two indexes and increment the first index and decrement the second index, until the indexes meet.

Example:

def reverseArray(arr, start, end): 
 
    while (start < end): 
        arr[start], arr[end] = arr[end], arr[start] 
        start += 1
        end = end-1

arr = [1, 2, 3, 4, 5, 6] 
reverseArray(arr, 0, 5)