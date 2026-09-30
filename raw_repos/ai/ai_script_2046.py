def sum_digits(n):
    sum = 0
    for i in range(1, n+1):
        digits = list(str(i))
        for digit in digits:
            sum += int(digit)
    return sum