def reverse_array(arr):
    left_index = 0
    right_index = len(arr) - 1

    while left_index < right_index:
        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
        left_index += 1
        right_index -= 1
    return arr

if __name__ == "__main__":
    print(reverse_array([1, 3, 4, 6, 8]))