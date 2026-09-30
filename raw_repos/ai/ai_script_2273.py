def is_palindrome(str):
    # reverse the string 
    rev_str = str[::-1] 
  
    # if string is equal then return true 
    if rev_str == str: 
        return True
    return False