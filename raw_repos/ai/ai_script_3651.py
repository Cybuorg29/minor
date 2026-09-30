class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.14

c = Circle(radius) 
print(c.area())  # Output: 95.033