def compute_combination(n, r):
    """
    Compute the number of ways for a host to select 'r' items from
    a list of 'n' options.

    Parameters
    ----------
    n : int
        The total number of items
    r : int
        The number of items to select

    Returns
    -------
    num : int
        The number of ways to select
    """
    num = 1

    # Calculate combination
    for i in range(r):
        num *= n - i
    num //= math.factorial(r)
    
    return num

n = 8
r =  3
print(compute_combination(n, r)) # Outputs 336