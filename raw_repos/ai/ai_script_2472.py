def divisible_by_each_other(num1, num2):
    """
    A function to check whether two numbers are divisible by each other
    """
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False

num1 = 8
num2 = 4

result = divisible_by_each_other(num1, num2)
print(result) # True