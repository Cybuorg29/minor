# Reverse an Array

def reverse_array(arr): 
    return [arr[i] for i in range(len(arr)-1, -1, -1)] 
  
# Driver program 
arr = [1, 2, 3, 4, 5] 
result = reverse_array(arr) 
print(result)