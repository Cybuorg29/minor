def min_coins(amount):
    # list of coin denominations
    coins = [1, 5, 10, 25]
    min_coins = 0
    i = len(coins) - 1
    while(amount > 0):
        if (amount >= coins[i]):
            amount -= coins[i]
            min_coins += 1
        else:
            i -= 1
    return min_coins

# Output
min_coins(amount)

# Output
7