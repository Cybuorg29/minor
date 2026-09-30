def bubble_sort(arr): 
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1): 
            for k in range(0, 3): 
                if arr[j][k] > arr[j+1][k] : 
                    arr[j][k], arr[j+1][k] = arr[j+1][k], arr[j][k]
  
arr = [[1, 5, 2], 
       [8, 4, 6], 
       [3, 7, 9]]

bubble_sort(arr)
print("Sorted matrix: ") 
for row in arr: 
    print(row)