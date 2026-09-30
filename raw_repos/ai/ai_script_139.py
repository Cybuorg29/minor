def calculate_series(x):
    """ Calculate the value of the mathematical series """
    result = 0
    for i in range(1, x + 1):
        result += (1 / (i * i))
    return result
    
if __name__ == "__main__":
    result = calculate_series(2)
    print(result) # prints 1.25