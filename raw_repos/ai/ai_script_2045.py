def heapsort(A):
    # step 1: create the heap
    heapify(A)

    # step 2: sort the heap
    for size in range(len(A), 1, -1):
        A[0], A[size - 1] = A[size - 1], A[0]
        sift_down(A, 0, size - 1)

    # step 3: return the sorted result
    return A