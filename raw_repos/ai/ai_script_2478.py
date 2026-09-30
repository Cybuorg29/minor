import json

data = {
  "name": "John", 
  "age": 25,
  "address": "123 Main Street"
}

userObject = json.loads(data)
print(userObject)