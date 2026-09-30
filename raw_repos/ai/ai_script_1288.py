# define a function to combine two lists into one
def combine_lists(list_1, list_2):
    # create a new list
    combined_list = []
    
    # append the elements from list 1
    for ele in list_1:
        combined_list.append(ele)

    # append the elements from list 2    
    for ele in list_2:
        combined_list.append(ele)
    
    # return the combined list
    return combined_list

# input two lists
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

# output the combined list
combined_list = combine_lists(list_1, list_2)
print("The combined list is " + str(combined_list))