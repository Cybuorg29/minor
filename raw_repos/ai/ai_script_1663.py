def sum_multiples(n):
    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

if __name__ == '__main__':
    print(sum_multiples(n))