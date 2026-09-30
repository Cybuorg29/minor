def reverseStr(str):
    revStr = "" 
    i = len(str) - 1
    while i >= 0: 
        revStr += str[i] 
        i = i - 1
    return revStr