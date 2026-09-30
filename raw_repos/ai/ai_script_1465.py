def prime_numbers(n): 
    numbers = list(range(2, n + 1)) 
    for i in range(2, n+1): 
        for j in range(i + 1, n+1): 
            if j % i == 0: 
                numbers[j - 2] = 0 
  
    return [number for number in numbers if number != 0]