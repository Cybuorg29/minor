def combineName(firstName, lastName):
    """
    A method that takes in two strings and combines them into a full name.
    Args: 
     firstName (str): first name 
     lastName (str): last name
    Returns:
     fullName (str): combined full name 
    """ 
    fullName = firstName + " " + lastName
    return fullName
    
if __name__ == '__main__':
    firstName = 'John'
    lastName = 'Smith'
    print(combineName(firstName, lastName))