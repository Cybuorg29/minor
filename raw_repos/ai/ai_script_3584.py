def printFibonacciSeries(n):
    a, b = 0, 1
    for i in range(0, n):
        print(a)
        c = a + b
        a = b
        b = c

printFibonacciSeries(10)