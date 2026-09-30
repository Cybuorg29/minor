def sum_of_cube_of_digits(num):
    sum = 0
    while (num > 0):
        digit = num % 10
        sum += digit**3
        num //= 10
    return sum