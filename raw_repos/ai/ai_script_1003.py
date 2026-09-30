def sum_of_digits(n): 
    # handle negative numbers 
    n = abs(n)

    # base case when n has only one digit
    if n < 10: 
        return n 

    # calculate the sum of the digits recursively  
    else: 
        return (n % 10 + sum_of_digits(int(n / 10))) 

print(sum_of_digits(13))