def longestString(str1, str2):
    if len(str1) > len(str2):
        longestString = str1
    else:
        longestString = str2
    return longestString

longestString = longestString("Hello", "World")
print(longestString)