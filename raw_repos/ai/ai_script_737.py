def printDivisorSum(num): 
   
    sum = 0
    i = 1
  
    while i <= num / 2: 
  
        if num % i == 0: 
            sum = sum + i 
        i = i + 1
  
    print("Sum of divisors of " + str(num) + " is " + str(sum)) 

num = 16
printDivisorSum(num)