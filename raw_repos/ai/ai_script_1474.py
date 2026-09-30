def addTwoNumbers(a, b):
    try:
        if type(a) == str or type(b) == str:
            raise TypeError('Inputs must be of type int or float')
        return a + b
    except TypeError as e:
        print(e)