def getMaxNumber():
    numbers = []
    
    num = int(input("Enter how many numbers: "))
    
    for i in range(num):
        numbers.append(int(input("Enter a number: ")))
        
    maxNum = max(numbers)
    print("The maximum number is", maxNum)