# Function to sort a list of numbers without using Python's built-in sort function
def my_sort(numbers):
    n = len(numbers)

    for i in range(n): 
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1] :
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                
    return numbers

# Example list
list = [3,5,4,2,1]
print(my_sort(list))