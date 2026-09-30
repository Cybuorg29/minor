def kthLargestCharacter(s, k):
  char_dict = {}
  for c in s:
    if c not in char_dict:
      char_dict[c] = 1
    else:
      char_dict[c] += 1

  char_list = sorted(char_dict.items(), key=lambda x : x[1], reverse = True)
  
  return char_list[k - 1][0]

print(kthLargestCharacter(s, k)) // l