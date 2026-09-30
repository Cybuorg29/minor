def capitalize_names(names):
 new_names = []
 for name in names:
    new_name = name[0].capitalize() + name[1:]
    new_names.append(new_name)
 return new_names