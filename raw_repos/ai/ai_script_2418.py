def lowercase_string(input_str):
    output_str = ""
    
    for char in input_str:
        output_str += char.lower()
    return output_str

if __name__ == '__main__':
    print(lowercase_string("HELLO WORLD"))