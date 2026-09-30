class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
        
    def distance(self, other_point):
        x1, y1 = self.x, self.y
        x2, y2 = other_point.x, other_point.y
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5