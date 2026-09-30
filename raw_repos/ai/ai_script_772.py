d = {'a':2, 'b':3, 'c':4}

def dictSum(d):
    total = 0
    for key in d:
        total += d[key]
    return total

if __name__ == "__main__":
    print(dictSum(d))