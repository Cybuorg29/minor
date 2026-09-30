def minimum_value(A):
    min=-float('inf')
    for a in A: 
        if a < min:
            min = a
    return min

print(minimum_value([6, 3, 9, 5, 8, -2, 10]))

# Output: -2