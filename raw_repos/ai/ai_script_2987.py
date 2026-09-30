def sum_of_list(lst, target):
    """
    This function takes a list and a target number as inputs, and prints only the list items whose total add up to the target number.
    """
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                print (lst[i], lst[j])

sum_of_list(list, target)