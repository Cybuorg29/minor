def convert12to24(time12h):
    # Check if last two elements of time is AM and first two are 12
    if time12h[-2:] == "AM" and time12h[:2] == "12": 
        return "00" + time12h[2:-2] 
          
    # If last two elements of time is AM
    elif time12h[-2:] == "AM": 
        return time12h[:-2] 
      
    # If last two elements of time is PM and first two are 12    
    elif time12h[-2:] == "PM" and time12h[:2] == "12": 
        return time12h[:-2] 
          
    else: 
          
        # add 12 to hours and remove AM
        return str(int(time12h[:2]) + 12) + time12h[2:8]