def is_palindrome(input_string):
    input_string = input_string.lower()
    if len(input_string) == 0:
        return False
    if len(input_string) == 1:
        return True

    if input_string[0] == input_string[-1]:
        return is_palindrome(input_string[1:-1])

    return False

# Usage 
string = 'RADAR'
result = is_palindrome(string)
print(result) # Output: True