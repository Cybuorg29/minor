def factorial(n): 
    res = 1 
    # Calculate value of 
    # factorial in for loop 
    for i in range(2,n+1): 
        res = res * i 
    return res 

n = 7
print("Factorial of",n,"is",factorial(n))