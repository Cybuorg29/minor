def authentication(username,password): 
    if username == "username" and password == "password": 
        print ("Login successful") 
    else: 
        print ("Incorrect username or password") 

username = input("Enter your username: ")
password = input("Enter your password: ")

authentication(username, password)