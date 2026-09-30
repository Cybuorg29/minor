def decimal_to_binary(num):
    binary = []

    while num > 0:
        binary.append(num%2)
        num //= 2
    binary.reverse()
    return binary