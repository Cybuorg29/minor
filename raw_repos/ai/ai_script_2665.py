def remove_short(mylist):
    mylist = [x for x in mylist if len(x) >= 3]
    return mylist
    
print(remove_short(mylist))
# Output: ['Apple', 'Hello']