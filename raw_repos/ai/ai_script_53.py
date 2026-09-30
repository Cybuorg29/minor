def binary_to_decimal(binary):
    decimal = 0 
    length = len(binary) 
    for digit in range(0, length): 
        decimal += int(binary[digit]) * pow(2, length - digit - 1) 
    return decimal 

print(binary_to_decimal("60"))
Output: 24