def removeDuplicates(txt):
    newTxt = []
    txt = txt.split()

    for x in txt:
        if x not in newTxt:
            newTxt.append(x)

    return " ".join(newTxt)