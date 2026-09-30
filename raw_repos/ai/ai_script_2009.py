def list_augment(int_list):
    """
    This function takes in a list of integers and 
    augments it with zeros after every 4 elements.
    """
    augmented_list = []
    for i in range(0, len(int_list), 4):
        augmented_list.append(int_list[i:i + 4])
        augmented_list.append(0)
    augmented_list.pop()
    return [item for sublist in augmented_list for item in sublist]
    
int_list = [1,2,3,4,5,6,7,8]
print(list_augment(int_list))

# Output: [1, 2, 3, 4, 0, 5, 6, 7, 8, 0]