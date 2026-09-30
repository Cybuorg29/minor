def check_divisible(value):
    """Check if value is divisible by 3 and 5."""
    # check if value is divisible by 3 and 5
    if value % 3 == 0 and value % 5 == 0:
        return True
    else:
        return False