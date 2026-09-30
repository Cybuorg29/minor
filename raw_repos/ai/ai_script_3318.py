import random

hex_arr = []
for i in range(5):
 rand_hex = random.randint(0, 255)
 hex_arr.append(hex(rand_hex))

print(hex_arr)