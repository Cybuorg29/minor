def median_num(n1, n2, n3):
    if n1 > n2 and n2 > n3:
        return n2
    elif n3 > n2 and n2 > n1:
        return n2
    elif n1 > n3 and n3 > n2:
        return n3
    elif n2 > n3 and n3 > n1:
        return n3
    elif n2 > n1 and n1 > n3:
        return n1
    else:
        return n1