def sum_even_numbers(n):
    '''This function will calculate the sum of all even numbers in the given range.'''
    total = 0
    for i in range(n):
        if i%2==0:
            total += i
    return total