def decimal_to_binary(num):

result = ""

while num > 0:
 remainder = num % 2 
 result = str(remainder) + result
 num = num // 2

return result