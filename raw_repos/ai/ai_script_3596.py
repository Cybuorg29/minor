def convert_base_10_to_base_8(number):
   binary_number = bin(number)[2:]
   octal_number = oct(int(binary_number, 2))[2:]
   return octal_number