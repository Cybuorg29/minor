# function to print Fibonacci sequence 
def fibo(n): 
    counter = 0
    a = 0
    b = 1
      
    while counter < n:
        print(a, end = " ")
        fibonacci = a + b 
        a = b 
        b = fibonacci 
        counter += 1
fibo(10)

Output: 0 1 1 2 3 5 8 13 21 34