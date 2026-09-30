def sum_without_plus(x,y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x

result = sum_without_plus(x, y)
print (result)
# Output: 30