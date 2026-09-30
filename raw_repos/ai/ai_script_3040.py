my_array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# A function to print second diagonal of 
# given array
def print_second_diagonal(arr): 
    # Find length of given array 
    n = len(arr)  
      
    # Traverse second diagonal 
    for i in range(0, n): 
        print(arr[i][n-1-i], end = " ") 
          
# Driver code 
print_second_diagonal(my_array)
# Output: 3 6 9