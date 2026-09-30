def heap_sort(data):  
    # Create an empty Max Heap
    max_heap = MaxHeap() 
    # Add elements to the Max Heap
    for element in data:
        max_heap.insert(element)
    
    sorted_data = []
    while max_heap.count > 0:
        # Pop the Maximum element from the Max Heap
        maximum = max_heap.extract_max()
        sorted_data.append(maximum)
 
    return sorted_data

sorted_data = heap_sort(data)
print(sorted_data) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]