class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        semi = (self.side1 + self.side2 + self.side3) / 2.0
        return (semi*(semi-self.side1)*(semi-self.side2)*(semi-self.side3)) ** 0.5