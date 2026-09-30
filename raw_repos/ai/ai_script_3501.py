# Define a python class 
class Person: 
 def __init__(self, firstname, lastname, address): 
  # make sure that firstname and lastname are provided when creating a new instance
  if (firstname == "" or lastname == ""): 
   raise ValueError("firstname and lastname can't be empty")
  self.firstname = firstname
  self.lastname = lastname
  self.address = address