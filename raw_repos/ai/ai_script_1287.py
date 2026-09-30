import random
def gen_string_arr(n):
    output = []
    for i in range(n):
        output.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)))
    return output