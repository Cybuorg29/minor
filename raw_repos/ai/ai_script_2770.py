class Car: 
    def __init__(self, color, make, model): 
        self.color = color 
        self.make = make 
        self.model = model 
    
    def start(self): 
        print("Engine started!") 

ford_mustang = Car('Red', 'Ford', 'Mustang') 
ford_mustang.start()