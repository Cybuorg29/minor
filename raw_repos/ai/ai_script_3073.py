def permutations(array):
    if len(array) == 0:
        return
    if len(array) == 1:
        return [array]
    perms = []
    for i in range(len(array)):
        elem = array[i]
        rem_perms = permutations(array[:i] + array[i+1:])
        for perm in rem_perms:
            perms.append([elem] + perm)
    return perms