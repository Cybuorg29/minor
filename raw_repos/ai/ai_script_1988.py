def findNumbers(N, M): 
    count = 0
    for i in range(1, N+1): 
        if i % 10 <= M: 
            count += 1
    return count