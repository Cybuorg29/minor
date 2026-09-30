def evenNumbers(m,n):
    evenNum=[]
    for i in range(m,n+1):
        if i%2 == 0:
            evenNum.append(i)
    return evenNum