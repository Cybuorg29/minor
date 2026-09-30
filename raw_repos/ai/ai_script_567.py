# Create a function to allocate resources to parties

def allocate(data):
    total = 0
    for item in data: 
        total += item[1] 
    allocation = [i[1]/total for i in data] 
    return allocation

print(allocate(data)) # [0.5, 0.3, 0.2]