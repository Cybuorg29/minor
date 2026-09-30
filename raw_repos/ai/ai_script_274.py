list = [14, 37, 54, 20]

def compute_sum(list):
    total_sum = 0
    for number in list:
        total_sum += number
    return total_sum

print(compute_sum(list))