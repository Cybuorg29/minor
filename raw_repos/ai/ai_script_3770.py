"""
Create an algorithm to compute the sum of the digits of a given positive integer.

Input: number (int)

Output: sum of the digits of the number (int)

"""
def compute_sum(number):
    if number < 0:
        return 0
    
    # get the last digit
    last_digit = number % 10
    
    # recursive call to get the sum of the remaining digits
    remainder_sum = compute_sum(number // 10)
    
    return last_digit + remainder_sum

if __name__ == '__main__':
    number = 9876
    print(compute_sum(number)) 
    # Output: 36