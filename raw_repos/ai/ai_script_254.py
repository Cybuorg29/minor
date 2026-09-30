def count_digit(num, digit):
    count = 0
    while num > 0:
        if num % 10 == digit:
            count += 1
        num //= 10
    
    return count

Number = 1234
Digit = 3
print(count_digit(Number, Digit))