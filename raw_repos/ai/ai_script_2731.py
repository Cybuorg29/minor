def filter_fruits(items):
    """This function takes a list of grocery items and generates a list containing only the fruits."""
    fruits = []
    for item in items:
        if item in ["apple", "banana", "grapes"]:
            fruits.append(item)
    return fruits

if __name__ == '__main__':
    items =["apple","banana","grapes","rice","onion"]
    fruits = filter_fruits(items)
    print(fruits)