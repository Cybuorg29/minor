def longest_common_substring(str1, str2):
    # keep track of the longest substring
    longest_substring = ""
    
    # iterate over each character in the first string
    for i in range(len(str1)):
        # iterate over each sub sequence of the first string
        for j in range(i+1, len(str1)+1):
            # compare the substring to each substring in the second string
            for k in range(len(str2)-(j-i)+1):
                # update longest_substring if we have a longer common substring
                if str1[i:j] == str2[k:k+(j-i)] and len(str1[i:j]) > len(longest_substring):
                    longest_substring = str1[i:j]

    return longest_substring