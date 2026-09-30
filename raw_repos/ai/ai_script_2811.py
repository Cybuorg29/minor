def upperCaseString(str): 
    res = "" 
    for i in range(len(str)):
        if i==0 or (str[i-1]==' '): 
            res = res + str[i].upper()
        else:
            res = res + str[i]
    return res 

str = "welcome to The world Of gEEks"
print(upperCaseString(str))