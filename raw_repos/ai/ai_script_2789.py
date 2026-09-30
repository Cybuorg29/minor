def rgb_to_hex(rgb_color):
    hex_code = ''
    for color in rgb_color:
        hex_code += f'{color:02x}'
    return hex_code

hex_code = rgb_to_hex(rgb_color) # hex_code = "ffe89a"