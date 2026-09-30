import json

data = { "1": "Apple", "2": "Orange", "3": {"A": "Banana", "B": "Grape"} }

data_json = json.dumps(data, indent=4)

print(data_json)