def print_multiplication_table(size):
    for i in range(1, size+1):
        for j in range(1, size+1):
            print(i*j, end="\t")
        print("\r")
 
print_multiplication_table(10)