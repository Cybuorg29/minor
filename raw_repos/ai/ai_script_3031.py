class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def speak(self, message):
    print(f"{self.name} says: {message}")