def greatestCommonFactor(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
 
    return num1
 
gcf = greatestCommonFactor(8, 32) 
print(gcf) 
 
# Output: 8