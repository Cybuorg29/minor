def print_binary(number): 
    binary_string = ""
    while number != 0: 
        remainder = number % 2
        binary_string = str(remainder) + binary_string
        number = number // 2
    return binary_string 

print(print_binary(number))