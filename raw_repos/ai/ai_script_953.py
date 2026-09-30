def appears_twice(lst, num):
    c = 0
    for n in lst:
        if n == num:
            c += 1
    if c > 2:
        return True
    else:
        return False