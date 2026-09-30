def remove_duplicates(lst):
    res = []
    for ele in lst:
        if ele not in res:
            res.append(ele)
    return res