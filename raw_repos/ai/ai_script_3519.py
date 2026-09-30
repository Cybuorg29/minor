import json

class Person:
 def __init__(self, json_string):
  data = json.loads(json_string)
  self.name = data['name']
  self.age = data['age']

myjson_string = '{"name": "John", "age": 20}'
person = Person(myjson_string)
print(person.name, person.age)