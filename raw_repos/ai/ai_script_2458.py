import json

json_data = '{"name":"John", "age":30}'

data = json.loads(json_data)

name = data["name"]
age = data["age"]

print(f"Name: {name}, Age: {age}")