sample_list = [1,2,3,4,5,6,7,8]

def remove_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            lst.remove(num)
    return lst

print(remove_even_numbers(sample_list))