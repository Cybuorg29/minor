The easiest way to check if a list of integers contains only even numbers is to iterate over the list and check if each element is divisible by 2. If all elements are divisible by 2, then the list contains only even numbers.


def check_even(nums):
    for num in nums:
        if num % 2 != 0:
            return False 
    return True
        

list_of_nums = [2, 4, 6]

result = check_even(list_of_nums)
print(result) # Output: True