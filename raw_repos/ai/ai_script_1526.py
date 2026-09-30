def permute(string):
  
  # base case
  if len(string) == 1:
    return [string]
  
  results = set()
  # iterate through each character in the string
  for i in range(len(string)):
    # select the ith character
    char = string[i]
    # generate all the permutations from the remaining characters
    remaining_characters = string[:i] + string[i+1:]
    permutations = permute(remaining_characters)
    # append the ith character to the beginning of each permutation and add to the result set
    for permutation in permutations:
      results.add(char + permutation)
  
  return list(results)

print(permute("ABC"))