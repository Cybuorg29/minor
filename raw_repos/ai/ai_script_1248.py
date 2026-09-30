def is_symmetrical(str1, str2):
    for i in range(0, len(str1)):
        if str1[i] != str2[-i-1]:
            return False
    return True