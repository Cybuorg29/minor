def compare_objects(object1, object2):
    for key, value in object1.items():
        if key in object2:
            if object1[key] != object2[key]:
                print("Different values for " + key + ": " + str(object1[key]) + " vs. " + str(object2[key]))
        else:
            print("New key not in second object: " + key)
    for key, value in object2.items():
        if key not in object1:
            print("New key not in first object: " + key)
    
compare_objects({"name": "John", "age": 30, "city": "New York"},
                {"name": "John", "age": 40, "city": "Las Vegas"})

# Output:
# Different values for age: 30 vs. 40
# New key not in first object: city