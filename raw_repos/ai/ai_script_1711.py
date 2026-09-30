def rightangle_triangles_pattern(n): 
    pattern = "" 
    
    
    for i in range(1,n+1): 
        for j in range(1,i+1): 
            pattern = pattern + " * "
        pattern = pattern + "\n"
  
   
    print(pattern) 
    
    
rightangle_triangles_pattern(5)