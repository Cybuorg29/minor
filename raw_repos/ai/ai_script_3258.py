def find_duplicates(lst):
    duplicate_elements = []
    for element in lst:
        if lst.count(element) > 1 and element not in duplicate_elements:
            duplicate_elements.append(element)
    return duplicate_elements

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 1]
    print(find_duplicates(lst))