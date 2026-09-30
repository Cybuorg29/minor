def factorial_(num):
    """Find the factorial of a given number"""

    # initialize the value of factorial
    factorial = 1

    # multiply the number with the numbers 
    # below its value to get the factorial
    for i in range(1, num+1):
        factorial *= i
    
    return factorial