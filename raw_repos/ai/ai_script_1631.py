def count_prime_num(x, y): 
  
    prime_count = 0
  
    for num in range(x, y + 1): 
       
       if num > 1: 
           for i in range(2, num): 
               if (num % i) == 0: 
                   break
           else: 
               prime_count += 1
  
    return prime_count 

print(count_prime_num(0, 100))