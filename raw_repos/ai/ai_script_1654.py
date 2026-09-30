def sort_by_age(data):
  return sorted(data, key=lambda k: k['age'], reverse=False)

sorted_list = sort_by_age(data)
print(sorted_list)