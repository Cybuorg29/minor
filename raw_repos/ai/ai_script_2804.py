def num_distinct_substrings(S, k):
   n = len(S)
   distinct_substrings = set()
   for i in range(n):
      for j in range(i+k, n+1):
         distinct_substring = "".join(sorted(list(set(S[i:j]))))
         distinct_substrings.add(distinct_substring)
   return len(distinct_substrings)