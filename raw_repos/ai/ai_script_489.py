# Function to calculate area of triangle  
def calculateArea(a, b, c): 
     
    # Calculating the semi-perimeter of triangle  
    s = (a + b + c) / 2
  
    # Calculate the area  
    area = (s*(s - a)*(s - b)*(s - c)) ** 0.5    
    
    return area 

# Driver code  
a = 5
b = 6
c = 7
print("Area of triangle is %0.2f" %calculateArea(a, b, c))