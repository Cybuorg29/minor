"""
Determine the index of an element in a given array using binary search.

Input: arr (list)  element (int)

Output: index (int)

"""
def binary_search(arr, element):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if element < arr[mid]:
            end = mid - 1
        elif element > arr[mid]:
            start = mid + 1
        else:
            return mid
    
    return -1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    element = 4
    print(binary_search(arr, element)) 
    # Output: 3