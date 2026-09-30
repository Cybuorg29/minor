"""
Create a function "calculate_area" which calculates the area of a polygon with three sides.
"""
def calculate_area(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    return (s*(s-s1)*(s-s2)*(s-s3)) ** 0.5