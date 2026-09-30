def bubblesort(arr):
    for i in range(len(arr)-1, 0, -1): 
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

my_list = [5, 1, 7, 3, 2]  
bubblesort(my_list) 
print(my_list)
# Output: [1, 2, 3, 5, 7]