def create_characterstic_dictionary(itemList):
    out = {}
    for item in itemList:
        out[item] = len(item)
    return out

if __name__ == '__main__':
    itemList = ["Apple", "Orange", "Grapes", "Bananas", "Watermelons"]
    print(create_characterstic_dictionary(itemList))