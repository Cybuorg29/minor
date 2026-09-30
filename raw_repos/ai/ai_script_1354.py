# Define the function to print array in reverse
def print_reverse(arr):
 
 # Base case
 if len(arr) == 0 :
  return

 # Print the last value
 print(arr.pop())

 # Recursive call with array - 1 
 return print_reverse(arr)

# Get the array
arr = [1,2,3,4]

# Print the array in reverse
print("The array in reverse is: ")
print_reverse(arr)