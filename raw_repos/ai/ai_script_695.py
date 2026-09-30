def Employee(name, age):
    return (name, age)

def print_details(employee):
    name, age = employee
    print(f"Name: {name}, age: {age}")