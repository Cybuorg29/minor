def get_permutations(s):
  """Get all possible permutations of a given set of characters."""
  n = len(s)
  result = []
  def recurse(i):
    if i == n:
      result.append(''.join(s))
      return
    for j in range(i, n):
      s[i], s[j] = s[j], s[i]
      recurse(i+1) # recurse over each character
      s[i], s[j] = s[j], s[i] # backtrack
  recurse(0)
  return result