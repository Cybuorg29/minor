# defining a function  
def add_ele(numbers): 
  
    # Initialize result 
    result = 0
    i = 0
  
    # Iterating elements in list  
    for i in range(len(numbers)): 
        result += numbers[i] 
    return result 
  
# Driver code 
numbers = [3, 6, 8, 12, 4, 19, 23, 12, 15, 10, 20]
print(add_ele(numbers))