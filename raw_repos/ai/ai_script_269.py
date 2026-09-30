def fibonacci(n):
    if n <= 0:
        return None 
    
    first = 0
    second = 1
    sequence = [first, second]
    for i in range(2, n):
        next_term = first + second
        sequence.append(next_term)
        first = second
        second = next_term
    return sequence