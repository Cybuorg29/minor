class Vehicle:
    def __init__(self, vehicle_type, make, model, color):
        self.type = vehicle_type
        self.make = make
        self.model = model
        self.color = color

car = Vehicle("Car", "Toyota", "Camry", "Red")