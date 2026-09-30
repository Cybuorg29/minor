def list_to_dict(tuples_list):
    result = {}
    for tuple_ in tuples_list:
        result[tuple_[0]] = tuple_[1]
    
    return result