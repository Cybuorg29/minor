def find_sum(n):  
    sum = 0
    for i in range (1, n): 
        if (i % 2 == 0): 
            sum = sum + i 
    return sum