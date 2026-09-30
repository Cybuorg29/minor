# Python program to calculate compound interest 

def compound_interest(principal, rate, time): 

    # Calculates compound interest 
    CI = principal * (pow((1 + rate / 100), time)) 

    print("Compound interest is", CI) 

# Driver Code 
compound_interest(2000, 0.09, 5)