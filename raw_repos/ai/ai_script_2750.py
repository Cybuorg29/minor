def stdev(data):
    avg = sum(data) / len(data)
    total = 0
    for x in data:
        total += (x - avg) ** 2
    return (total / (len(data) - 1)) ** 0.5