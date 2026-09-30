def div(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    else:
        return x // y