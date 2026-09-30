def separate_even_odd(arr):
 even = []
 odd = []
 for i in arr:
 if i % 2 == 0:
 even.append(i)
 else:
 odd.append(i)
 return even, odd

print(separate_even_odd([3, 6, 9, 12, 21]))
# Output: ([6, 12], [3, 9, 21])