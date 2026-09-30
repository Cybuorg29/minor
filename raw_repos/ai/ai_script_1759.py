def bin_to_hex(binary_string):
    dec = int(binary_string, 2)
    hex_string = hex(dec).replace('x', '')
    return hex_string