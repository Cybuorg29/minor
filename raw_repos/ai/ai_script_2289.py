# Algorithm to reverse a string
def reverse_string(s):
# Create a result string
 result = ""
 # Iterate through the string in reverse order
 for i in range(len(s)-1, -1, -1):
 result += s[i]
return result