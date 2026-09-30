A better algorithm for calculating Fibonacci sequence is the iterative method. Instead of making recursive calls, this method computes each element of the Fibonacci sequence in a loop. This method is more efficient and requires less memory overhead. The algorithm is as follows:

def iterative_fibonacci(n):
    a = 0
    b = 1
    for i in range(1,n+1):
        c = a + b
        a = b
        b = c
    return a