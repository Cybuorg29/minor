import re 
  
def check(password): 
  
    #Define pattern rules
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}"
      
    if (re.search(pattern,password)): 
        return True
    else: 
        return False 
  
# Driver code     
password = "Geronimo1"
if (check(password)): 
    print("Valid Password") 
else: 
    print("Invalid Password")