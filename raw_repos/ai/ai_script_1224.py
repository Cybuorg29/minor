def operate(operation, a, b):
    if operation == 'addition':
        return a + b
    elif operation == 'subtraction':
        return a - b
    else:
        return 'Invalid operation.'

print(operate('addition', 4, 20)) # prints 24