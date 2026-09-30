def isArmstrong(num):
 s = 0
 temp = num
 while temp > 0:
 digit = temp % 10
 s += digit ** 3
 temp //= 10
 if num == s:
 return True
 else:
 return False

for num in range(lower, upper + 1):
 if isArmstrong(num):
 print(num)