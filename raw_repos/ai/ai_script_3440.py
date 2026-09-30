def maximum_of_three(x, y, z): 
    if x > y and x > z: 
        max = x 
    elif y > x and y > z: 
        max = y 
    else: 
        max = z 
    return max