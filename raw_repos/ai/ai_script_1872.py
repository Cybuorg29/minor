def is_palindrome(arr):
  rev_arr = arr[::-1]
  if arr == rev_arr:
    return True
  else:
    return False

print(is_palindrome([1, 2, 3, 2, 1]))