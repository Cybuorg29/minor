def categorize_numbers(lst):
 odd = []
 even = []
 for num in lst:
  if num % 2 == 0:
   even.append(num)
  else:
   odd.append(num)
 return odd, even