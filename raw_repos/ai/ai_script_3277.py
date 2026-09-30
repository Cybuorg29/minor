def find_sec_largest(arr):
  max1 = max(arr[0], arr[1])
  max2 = min(arr[0], arr[1])

#Iterate over the array to find max2 and max1
for i in range(2, len(arr)):
  if arr[i] > max1:
    max2 = max1
    max1 = arr[i]
  elif arr[i] > max2 and arr[i]!=max1:
    max2 = arr[i]
  else:
    continue

# else return the second max
return max2