"""
Create a class that can represent a 2D coordinate system
"""
class CoordinateSystem:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  def add(self,other):
    x = self.x + other.x
    y = self.y + other.y
    return CoordinateSystem(x,y)

if __name__ == '__main__':
    a = CoordinateSystem(1,2)
    b = CoordinateSystem(3,4)
    print(a.add(b)) # <__main__.CoordinateSystem object at 0x000002B50FE37B70>