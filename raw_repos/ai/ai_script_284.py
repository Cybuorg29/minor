def name_length_dict(names):
    name_length_dict = dict()
    for name in names:
        name_length_dict[name] = len(name)
    return name_length_dict 

name_length_dict(names)