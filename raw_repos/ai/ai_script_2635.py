def permutations(nums):
    if len(nums) == 0:
        return []

    if len(nums) == 1:
        return [[nums[0]]]
    
    perms = []

    for i, n in enumerate(nums):
        sub_perms = permutations(nums[:i] + nums[i+1:])

        for perm in sub_perms:
            perms.append([n] + perm)

    return perms