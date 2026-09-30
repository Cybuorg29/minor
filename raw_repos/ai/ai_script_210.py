def print_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=' ')
        temp = a 
        a = b 
        b = temp + b

# The output of the function would be
# 0 1 1 2 3 5 8