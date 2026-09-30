def string_inverse(string): 
    inverse_string = ""
    for i in range(len(string)-1, -1, -1):
        inverse_string += string[i]
    return inverse_string

# Test program
string = "Hello World!"
inverse_string = string_inverse(string)

print("Original String: %s" % string)
print("Inverse String: %s" % inverse_string)

# Output
# Original String: Hello World!
# Inverse String: !dlroW olleH