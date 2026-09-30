def sort_dict_list(animals):
    sorted_animals = sorted(animals, key=lambda k: k['age'])  
    return sorted_animals

result = sort_dict_list(animals)
print(result)
# Output: [{'name': 'Fish', 'age': 1}, {'name': 'Cat', 'age': 3}, {'name': 'Dog', 'age': 5}, {'name': 'Deer', 'age': 8}]