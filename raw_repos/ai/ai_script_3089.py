# Function to randomly rearrange the elements of the given array
import random 
def shuffle_array(nums):
    # Initialize a result array
    result = nums.copy()
    
    # Iterate over the array
    for i in range(len(nums)): 
        # Generate a random index between 0 and the current index
        j = random.randrange(0, i + 1)
        
        # Swap elements at the current and random indices
        result[i], result[j] = result[j], result[i] 
        
    # Return the result array
    return result

# Test the function by printing the shuffled array
print(shuffle_array(nums))