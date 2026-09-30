class Hospital:
    def __init__(self, location, name, rooms, staff):
        self.location = location
        self.name = name
        self.rooms = rooms
        self.staff = staff
    
    def get_location(self):
        return self.location
    
    def get_name(self):
        return self.name
    
    def get_rooms(self):
        return self.rooms
    
    def get_staff(self):
        return self.staff
    
    def set_location(self, location):
        self.location = location
    
    def set_name(self, name):
        self.name = name
    
    def set_rooms(self, rooms):
        self.rooms = rooms
    
    def set_staff(self, staff):
        self.staff = staff