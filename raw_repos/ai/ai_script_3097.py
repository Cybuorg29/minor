import json

def convert_json_string(string):
    return json.loads(string)

convert_json_string(string) # Returns { "a": 1, "b": 2, "c": 3 }