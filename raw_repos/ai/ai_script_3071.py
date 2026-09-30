def convert_to_tuple(lst):
    tup = [(x['name'], x['age']) for x in lst]
    return tuple(tup)