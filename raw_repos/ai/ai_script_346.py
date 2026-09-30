def remove_condition(lst, condition):
    return [x for x in lst if not condition(x)]