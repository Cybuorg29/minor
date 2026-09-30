import itertools
flattened_list = list(itertools.chain.from_iterable(nested_list))
print(flattened_list)
# Output: [1, 2, 3, 4, 5, 6]