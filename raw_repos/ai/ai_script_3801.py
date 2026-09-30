input_string = 'Hello World!'

def reverse_string(input_string):
    if len(input_string) == 0:
        return "" 
    else:
        return reverse_string(input_string[1:]) + input_string[0] 
 
res = reverse_string(input_string) 
print(res)