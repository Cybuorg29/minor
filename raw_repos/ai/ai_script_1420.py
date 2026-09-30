def bubble_sort(arr):
  for _ in range(len(arr) -1): 
    for i in range(len(arr)-1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
print(bubble_sort([4, 8, 1, 3, 9])) # [1, 3, 4, 8, 9]