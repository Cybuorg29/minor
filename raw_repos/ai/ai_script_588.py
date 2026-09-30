def printPalindromicNumbers(n): 
    for num in range(1, n + 1):
        s = str(num)
        if(s == s[::-1]):
            print(num, end=" ")

printPalindromicNumbers(100)