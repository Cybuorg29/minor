def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    """
    Function to calculate the area of a triangle given the coordinates of its 3 vertices
    """
    a = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    b = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
    c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
    s = (a + b + c) / 2
    return ((s*(s-a)*(s-b)*(s-c))**0.5)
    
if __name__ == "__main__":
    x1 = 1
    y1 = 5
    x2 = 4
    y2 = 3
    x3 = 7
    y3 = 2
    print(calculate_triangle_area(x1, y1, x2, y2, x3, y3))
    # should print 4.24