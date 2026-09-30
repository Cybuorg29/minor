def gen_list_of_consecutive_numbers(n):
    """Generate a list of consecutive natural numbers up to a given number n"""
    return list(range(1, n + 1))

if __name__ == '__main__':
    n = 8
    print(gen_list_of_consecutive_numbers(n))