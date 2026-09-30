def fibonacci(n):
    fib_list = [1]
    if n == 1:
        return fib_list
    else:
        fib_list.append(1)
        while len(fib_list) < n:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list