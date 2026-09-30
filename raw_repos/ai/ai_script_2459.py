def adjacent_numbers(array):
    # Create a set of all possible adjacent numbers
    # and add each array element to the set
    adjacent_set = set()
    for sublist in array:
        for element in sublist:
            adjacent_set.add(element)
 
    # Iterate over each array element and its neighbours
    for i in range(len(array)):
        for j in range(len(array[0])):
            # Check if the neighbour (left, right, top, bottom) exists
            if i+1 < len(array):
                adjacent_set.add(array[i+1][j])
            if i-1 >= 0:
                adjacent_set.add(array[i-1][j])
            if j+1 < len(array[0]):
                adjacent_set.add(array[i][j+1])
            if j-1 >= 0:
                adjacent_set.add(array[i][j-1])
 
    # Remove the original elements from the set
    for elem in array:
        for a in elem:
            adjacent_set.remove(a)
 
    return list(adjacent_set)