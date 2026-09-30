def find_max(arr, target): 
  dp = [[False for i in range(target + 1)] for j in range(len(arr))]
  for i in range(len(arr)):
      dp[i][0] = True
  for i in range(1, len(arr)): 
    for j in range(1, target + 1): 
      if dp[i - 1][j]: 
          dp[i][j] = dp[i - 1][j] 
      elif j >= arr[i]: 
          dp[i][j] = dp[i - 1][j - arr[i]] 
  max_val = 0
  for i in range(1, target + 1): 
    if dp[len(arr) - 1][i]: 
      max_val = max(max_val, i) 
  return max_val