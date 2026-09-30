# Import the random module
import random

# Generate 1000 random numbers 
random_numbers = [random.randint(1, 1000) for i in range(1000)]

# Calculate mean of the random numbers
mean = sum(random_numbers)/len(random_numbers)

# Print mean of random numbers
print("The mean of 1000 random numbers is: ", mean)