def get_longest_palindrome(s):
    longest_palindrome = ''
    s_length = len(s)
    for i in range(s_length):
        for j in range(i, s_length):
            substring = s[i:j + 1]
            if len(substring) > len(longest_palindrome) and substring == substring[::-1]:
                longest_palindrome = substring
    return longest_palindrome

# Verify it works
print(get_longest_palindrome('kayakracecar'))