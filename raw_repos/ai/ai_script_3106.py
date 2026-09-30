def generateId(string):
    hashValue = hash(string)
    id = 0
    while hashValue > 0:
        id += hashValue % 10
        hashValue //= 10
    return id