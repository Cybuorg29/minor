def f(arr):
    arr_copy = arr[::]
    arr_copy.remove(arr_copy[0])
    return arr_copy