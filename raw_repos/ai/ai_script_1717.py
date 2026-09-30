def get_max_value(d):
    """Calculate the maximum value in a dictionary."""
    max_value = 0
    for key in d:
        if d[key] > max_value:
            max_value = d[key]
    return max_value