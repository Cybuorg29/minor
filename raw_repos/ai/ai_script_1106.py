def find_sum(lst):
    """Return the sum of a given list of numbers."""
    res = 0
    for x in lst:
        res += x
    return res # was missing, was iterating over list instead of lst.