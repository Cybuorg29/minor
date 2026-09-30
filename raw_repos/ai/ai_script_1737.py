def permute(string):
    if len(string) == 1:
        return [string] 

    prevList = permute(string[1:]) 

    nextList = [] 
    for i in range(len(prevList)): 
        for j in range(len(string)): 
            newString = prevList[i][:j] + string[0:1] + prevList[i][j:] 
            if newString not in nextList: 
                nextList.append(newString) 
    return nextList