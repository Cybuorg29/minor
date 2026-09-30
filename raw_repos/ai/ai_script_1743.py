def Fibonacci(n):
    if n==0 or n==1:
        return n 
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

def Fibonacci_Series(max_num):
    for n in range(max_num+1):
        print(Fibonacci(n))

# Output: 0 1 1 2 3 5