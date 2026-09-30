def get_num_elements(data):
    count = 0
    for item in data:
        count += 1
    return count

data = [{"name":"John"},{"name":"Bob"},{"name":"Alice"}]
print(get_num_elements(data))