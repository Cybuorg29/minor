def remove_duplicates(mylist):
    mylist = list(dict.fromkeys(mylist))
    return mylist

if __name__ == '__main__':
    mylist = [1, 2, 3, 2, 4, 2]
    print(remove_duplicates(mylist))