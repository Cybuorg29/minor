list1 = [4, 3, 4, 2, 3, 4, 4]

def delete_four(arr):
    """This function deletes all occurrences of the number 4 in the given array"""
    for i in range(len(arr)):
        if arr[i] == 4:
            arr.pop(i)
            i -= 1
    return arr

print(delete_four(list1))