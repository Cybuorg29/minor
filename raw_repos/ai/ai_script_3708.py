def sqrt(number):
    x = number
    y = 1
    epsilon = 0.000001
    while x-y > epsilon:
        x = (x + y)/2
        y = number/x
    return x

sqrt(number) # returns 2.0