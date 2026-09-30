import json

data = [
    {
        "id": "12345",
        "model": "Honda",
        "year": 2021
    }
]

data[0]["color"] = "red"

json_object = json.dumps(data, indent = 4)
print(json_object)

Output: 
[
    {
        "id": "12345",
        "model": "Honda",
        "year": 2021,
        "color": "red"
    }
]