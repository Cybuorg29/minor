def generate_permutations(n): 
  
    if n == 0: 
        return [] 
    
    if n == 1: 
        return [[1]] 
  
    permutations = [] 
    for i in range(n): 
        permutations_n_1 = generate_permutations(n - 1) 
  
        for perm in permutations_n_1: 
            for j in range(n): 
                r = perm.copy() 
                r.insert(j, n) 
                permutations.append(r) 
  
    return permutations