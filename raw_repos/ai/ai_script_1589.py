def find_gcd(x,y):
   
    # If x is greater than y
    # Swapping the x and y
    if x > y:
        tmp = x
        x = y
        y = tmp

    while y > 0:
        tmp = y
        y = x % y
        x = tmp
    return x

gcd = find_gcd(20,12)
print("The greatest common divisor of 20 and 12 is: ", gcd)