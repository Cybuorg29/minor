def myDict(myList3):
    result = {}
    for i in myList3:
        result[i] = i**2
    return result

myDict = myDict(myList3)
print(myDict)