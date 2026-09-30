class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print("Hi, my name is %s and I am %d years old." % (self.name, self.age))