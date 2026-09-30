class Cube(object):
    
    def __init__(self, side_length):
        self.side_length = side_length
    
    
    def calculate_volume(self):
        return self.side_length * self.side_length * self.side_length