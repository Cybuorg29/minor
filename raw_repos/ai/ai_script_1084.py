import string 
import random 

def generate_password(length): 
    # Generate a random string of characters 
    letters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(letters) for i in range(length)) 
  
    return password
  
# Driver Code
length = 8
print(generate_password(length))