def replace_value(mylist, old_value, new_value):
    if old_value in mylist:
        mylist[mylist.index(old_value)] = new_value
    return mylist