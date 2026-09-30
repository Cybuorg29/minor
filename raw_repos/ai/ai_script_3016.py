import json

resp = '[{"name": "john", "age": 25}, {"name": "Anna", "age": 17}, {"name": "Rick", "age": 46}]'

data = json.loads(resp)
print(len(data)) # 3 objects