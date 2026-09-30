def longest_common_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    result = 0
    dp = [[0 for x in range(len2+1)] for x in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0
    return result