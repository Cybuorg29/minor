def is_palindrome(string): 
    left = 0
    right = len(string) - 1
  
    while right >= left: 
        if string[left] != string[right]: 
            return False
        left += 1
        right -= 1
    return True