import math
def split_list(a_list):
    mid_point = int(math.floor(len(a_list) / 2))
    first_half = a_list[:mid_point]
    second_half = a_list[mid_point:]
    return first_half, second_half