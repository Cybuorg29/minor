def iterateMyList(myList):
    iterator = iter(myList)
    while True:
        try: 
            print(next(iterator))
        except StopIteration: 
            break