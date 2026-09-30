# Find the smallest missing positive number
def smallest_positive(arr): 
 s = set(arr) 
 i = 1 
 while i in s: 
 i += 1
 return i

arr = [-2, 0, 1, 3] 
smallest = smallest_positive(arr)
print(smallest) # 2