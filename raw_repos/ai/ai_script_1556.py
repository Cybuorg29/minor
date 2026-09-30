class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"This is a rectangle with width of {self.width} and height of {self.height}."