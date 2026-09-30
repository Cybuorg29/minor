def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    return num % 2