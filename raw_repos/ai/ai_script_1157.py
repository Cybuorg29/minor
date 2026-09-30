def binary_to_decimal(binary): 
    decimal = 0
    base = 1
    binary = str(binary)
    length = len(binary) 
    for i in range(length-1, -1, -1): 
        if (binary[i] == '1'):      
            decimal += base
        base = base * 2
    return decimal