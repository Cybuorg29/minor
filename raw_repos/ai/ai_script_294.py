def smallest_window(str1, str2):
 min_str = ""
 min_size = float("inf")
 
 for i in range(len(str1)):
  for j in range(i+1, len(str1)):
   curr_str = str1[i:j+1]
   count = 0
   for ch in str2:
    if ch in curr_str:
     count += 1
   if len(curr_str) < min_size and count == len(str2):
    min_str = curr_str
    min_size = len(curr_str)
 return min_str
 
print(smallest_window("abcde", "ade"))