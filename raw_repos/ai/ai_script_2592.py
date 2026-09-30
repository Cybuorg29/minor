def print_multiplication_table(n): 
    for i in range(1, n+1): 
        for j in range(1, n+1): 
            print(i*j, end="\t") 
        print("\n") 

print_multiplication_table(4)

Output:
1	2	3	4	
2	4	6	8	
3	6	9	12	
4	8	12	16