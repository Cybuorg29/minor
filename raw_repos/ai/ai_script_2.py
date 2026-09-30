def greetings(name):
    # assert name is a string
    assert isinstance(name, str), "name must be a string"
    num = 5
    # "message" variable should be defined before using it 
    message = "Hello, " + name + "!"
    return message