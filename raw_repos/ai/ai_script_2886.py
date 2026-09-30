def get_sum(x, y):
    # get the lower bound and upper bound
    lower, upper = min(x, y), max(x, y)

    # apply the arithmetic series formula
    return (upper * (upper + 1) - lower * (lower - 1)) // 2