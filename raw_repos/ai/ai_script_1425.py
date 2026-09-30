"""
Create a program to create a list of all the numbers from 1 to 10 which are divisible by 3
"""

def divisible_by_three():
    divisible_by_three_list = []
    for i in range(1, 11):
        if i % 3 == 0:
            divisible_by_three_list.append(i)
    return divisible_by_three_list

if __name__ == '__main__':
    print(divisible_by_three())