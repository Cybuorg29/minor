def find_two_numbers(my_list, sum):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] + my_list[j] == sum:
                return my_list[i], my_list[j]

find_two_numbers(my_list, sum);