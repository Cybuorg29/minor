def base10_to_binary(n):

    # Create an empty binary array
    binary_arr = [0] * (int(math.log2(n)) + 1) 
  
    # Iterate through binary array
    for i in range(len(binary_arr) - 1, -1, -1): 
        if n >= pow(2, i): 
            n -= pow(2, i) 
            binary_arr[len(binary_arr) - i - 1] = 1
  
    return binary_arr 
  
# Driver Code 
n = 8
print(base10_to_binary(n)) # [1, 0, 0, 0]