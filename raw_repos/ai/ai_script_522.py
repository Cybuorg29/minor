import itertools

combinations = [''.join(i) for i in itertools.product(chars)]

# Output: ["a", "b", "c", "ab", "ac", "ba", "bc", "ca", "cb", "abc", "acb", "bac", "bca", "cab", "cba"]