class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        s = (self.side_a+self.side_b+self.side_c)/2
        return (s*(s-self.side_a)*(s-self.side_b)*(s-self.side_c)) ** 0.5

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_angles(self):
        a = (self.side_b**2 + self.side_c**2 - self.side_a**2)/(2*self.side_b*self.side_c)
        b = (self.side_a**2 + self.side_c**2 - self.side_b**2)/(2*self.side_a*self.side_c)
        c = (self.side_b**2 + self.side_a**2 - self.side_c**2)/(2*self.side_b*self.side_a)
        return [a, b, c]