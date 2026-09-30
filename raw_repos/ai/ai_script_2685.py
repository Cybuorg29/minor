import json

def deep_copy(obj):
    return json.loads(json.dumps(obj))