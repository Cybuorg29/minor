"""
Find the two largest numbers in an array and return them in reverse order
""" 

array = [7,2,9,3,1,5]

def largest_numbers(array):
    largest = 0
    second_largest = 0
    for i in array:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest:
            second_largest = i
    return [largest, second_largest]
 
if __name__ == '__main__':
    print(largest_numbers(array))