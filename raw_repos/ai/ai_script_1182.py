def binToDecimal(num): 
    # Initializing base  
    # value to 1, i.e 2^0 
    base = 1; 
      
    dec_val = 0; 
      
    # Extracting digits of  
    # binary number from   
    # the right most side 
    # and keeping  
    # incrementing the base 
    # by multiply of 2 
    temp = num 
    while(temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
          
        dec_val += last_digit * base; 
        base = base * 2; 
      
    return dec_val
num = 11100011
print('Decimal Equivalent of',num,'is',binToDecimal(num))