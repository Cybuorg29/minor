def encrypt_string(string):
    encrypted_string = "" 

    for char in string:
        encrypted_string += chr(ord(char) + 5)

    return encrypted_string