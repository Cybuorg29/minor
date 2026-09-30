def gcm(x, y): 
    if(x > y): 
        gcm = x 
    else: 
        gcm = y 
  
    while(True): 
        if((gcm % x == 0) and (gcm % y == 0)): 
            return gcm 
        gcm = gcm + 1
  
# Driver Program 
x = 12
y = 18
print(gcm(x, y))