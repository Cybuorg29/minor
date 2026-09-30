def unpack_tuples(tuples):
    names, ages = zip(*tuples)
    return list(names), list(ages)

if __name__ == '__main__':
    names, ages = unpack_tuples(tuples)
    print(names)
    print(ages)