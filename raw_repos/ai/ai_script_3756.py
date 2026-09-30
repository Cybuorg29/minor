def compare_strings(string1, string2):
    i = 0
    length = min(len(string1), len(string2))

    while i < length:
        if string1[i] < string2[i]:
            return 'smaller'
        elif string1[i] > string2[i]:
            return 'bigger'
        i += 1
    
    if len(string1) > len(string2):
        return 'bigger'
    else:
        return 'equal'