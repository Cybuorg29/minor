def sort_list(mylist):
    for i in range(len(mylist)):
        min_idx = i
        for j in range(i+1, len(mylist)):
            if mylist[min_idx] > mylist[j]:
                min_idx = j
        mylist[i], mylist[min_idx] = mylist[min_idx], mylist[i]
    return mylist