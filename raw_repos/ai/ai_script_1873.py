def rearrange(string):
    Frequency={}
    newstr=''
    for c in string:
        if c not in Frequency:
            Frequency[c] = 1
        else:
            Frequency[c] = Frequency[c]+1
    for key,value in sorted(Frequency.items(), key=lambda x: x[1], reverse=True):
        for i in range(value):
            newstr = newstr+key
    return newstr