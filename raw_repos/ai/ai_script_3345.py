def group_arrays(array, conditions):
    groups = []
    for condition in conditions:
        group = [x for x in array if condition(x)]
        groups.append(group)
    return groups