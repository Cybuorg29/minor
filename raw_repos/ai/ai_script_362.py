def generate_key_value(arr):
    key_val_pairs = {k:v for k,v in enumerate(arr)}
    return key_val_pairs

print(generate_key_value(arr))

Output:
{0: 1, 1: 2, 2: 3, 3: 4}