def fibonacci_sum(number):
    fib_list = [0,1]
    while True:
        next_number = fib_list[-1] + fib_list[-2]
        if next_number > number:
            break
        fib_list.append(next_number)
    return sum(fib_list[:-1])