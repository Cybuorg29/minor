def factorial(n):
    fact = 1
    for i in range(1, n+1): 
        fact = fact*i % 10**10
    return fact % 10**10