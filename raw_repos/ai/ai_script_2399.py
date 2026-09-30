def edit_distance(str1, str2):
    edits = 0
    m = len(str1)
    n = len(str2)
    if m < n:
        for i in range(m, n):
            edits += 1
        for i in range(m):
            if str1[i] != str2[i]:
                edits += 1
    else:
        for i in range(n, m):
            edits += 1
        for i in range(n):
            if str1[i] != str2[i]:
                edits += 1
    return edits