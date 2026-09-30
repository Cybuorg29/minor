def searchTree(T, k):
    if not T:
        return False

    if k == T[0]:
        return True
    elif k < T[0]:
        return searchTree(T[1], k)
    else:
        return searchTree(T[2], k)