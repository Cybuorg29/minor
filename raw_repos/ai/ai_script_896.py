"""
Create a function to compute the area of a triangle when the length of its three sides are known
"""

def TriangleArea(a, b, c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area

a, b, c = 6, 8, 10

print(TriangleArea(a, b, c)) # print 24.0