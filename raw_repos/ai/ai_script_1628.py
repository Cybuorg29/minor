def sort_list(my_list):
    """Function to sort the list in increasing order"""
    for i in range(len(my_list)):
        min_idx = i
        for j in range(i+1, len(my_list)):
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list
    
if __name__ == '__main__':
    my_list = [3, 4, 2, 6]
    sorted_list = sort_list(my_list)
    print(sorted_list)  # [2, 3, 4, 6]