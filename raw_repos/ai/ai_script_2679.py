def find_pair(lst, target_sum):
    """
    Given a list of integers and a target sum, 
    this function returns a pair of said integers 
    that add up to the target sum.
    """
    seen = set()
    for num in lst:
        inverse = target_sum - num
        if inverse in seen:
            return (num, inverse)
        seen.add(num)