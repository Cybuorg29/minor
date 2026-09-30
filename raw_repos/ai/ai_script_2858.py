def cipher(input_str, key):
  output_str = ""

  for char in input_str:
    if char.isalpha():
      # Encrypt each character
      ascii_value = ord(char)
      ascii_value = ascii_value + (key % 26)
      if char.isupper():
        if ascii_value > ord("Z"):
          ascii_value -= 26
      elif char.islower():
        if ascii_value > ord("z"):
          ascii_value -= 26  
      output_str += chr(ascii_value)
    else:
      output_str += char

  return output_str

if __name__ == '__main__':
  # Sample input
  input_str = 'Hello World!'
  key = 5
  print('Original input: {}'.format(input_str))

  # Encryting the string
  cipher_str = cipher(input_str, key)
  print('Encrypted input: {}'.format(cipher_str))

  # Decrypting the string
  plain_text = cipher(cipher_str, -key)
  print('Decrypted input: {}'.format(plain_text))