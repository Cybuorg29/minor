def identify_value_type(val):
    if type(val) is int:
        return 'int'
    elif type(val) is float:
        return 'float'
    elif type(val) is str:
        return 'str'
    elif type(val) is list:
        return 'list'
    elif type(val) is dict:
        return 'dict'