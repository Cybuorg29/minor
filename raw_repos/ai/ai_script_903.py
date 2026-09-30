def quicksort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        pivot = arr[0]
        arr.remove(arr[0])
        left_arr = []
        right_arr = []
        for element in arr:
            if element <= pivot:
                left_arr.append(element)
            else:
                right_arr.append(element)
        left_arr = quicksort(left_arr)
        right_arr = quicksort(right_arr)
        sorted_arr = left_arr + [pivot] + right_arr
        return sorted_arr

if __name__ == "__main__":
    array = [2, 4, 5, 1, 9, 0]
    sorted_arr = quicksort(array)
    print(sorted_arr)

# Output: [0, 1, 2, 4, 5, 9]