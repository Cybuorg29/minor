import hashlib

def generate_hash(my_dict):
    my_string = str(my_dict)
    res = hashlib.md5(my_string.encode()).hexdigest() 
    
    return res

print(generate_hash(my_dict))