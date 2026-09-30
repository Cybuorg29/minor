def generate_json(data):
    return json.dumps(data)
    
# Usage 
data = {"name": "John Doe", "age": 25, "address": "123 Main St."}
json_str = generate_json(data) 
print(json_str)