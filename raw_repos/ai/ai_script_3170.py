def intersection(list1, list2):
    # Initialize an empty list 
    intersection_list = []

    # Iterate over elements of the first list
    for num in list1:
        # Compare each element of first list with elements of second list
        if num in list2:
            # Add to the intersection list if matches
            intersection_list.append(num)

    return intersection_list

if __name__ == "__main__":
    list1 = [2, 5, 9, 12, 17]
    list2 = [3, 5, 9, 10]
    print(intersection(list1, list2))