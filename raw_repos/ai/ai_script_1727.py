def change(n, coins): 
    m = len(coins) 
    table = [[0 for x in range(m)] for x in range(n+1)] 

    # Fill the entries for 0 value case (n = 0) 
    for i in range(m): 
        table[0][i] = 1

    # Fill rest of the table entries in bottom-up manner 
    for i in range(1, n+1): 
        for j in range(m): 
            # Count of solutions including coins[j] 
            x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0

            # Count of solutions excluding coins[j] 
            y = table[i][j-1] if j >= 1 else 0 

            # total count 
            table[i][j] = x + y 
    return table[n][m-1]