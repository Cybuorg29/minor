def get_multiples(n, limit):
    """Return list of n's multiples for all numbers up to limit"""
    multiples = []
    for i in range(limit + 1):
        if i % n == 0:
            multiples.append(i)  
    return multiples