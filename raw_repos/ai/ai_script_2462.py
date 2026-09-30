def find_multiples(base, lower, upper):
    output = []
    for i in range(lower, upper+1):
        if i % base == 0:
            output.append(i)
    return output