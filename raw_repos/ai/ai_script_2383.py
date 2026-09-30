# Calculate Minimum Element
def find_min(arr):
    # Set a variable to store the minimum element of the array 
    minimum = arr[0] 
    # Compare each element of the array with the current min element 
    for i in range(1, len(arr)): 
        if arr[i] < minimum: 
            minimum = arr[i] 
    return minimum 

# Main Program
array = [2,3,5,1,4]
result = find_min(array)
print(result)