def sum_even(num):
    total = 0 
    for i in range(1, num+1):
        if i % 2 == 0:
            total += i
    return total

if __name__ == "__main__":
    print(sum_even(50))