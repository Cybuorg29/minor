def powerset(s):
    result = [[]]
    for x in s:
        result.extend([y + [x] for y in result])
    return result