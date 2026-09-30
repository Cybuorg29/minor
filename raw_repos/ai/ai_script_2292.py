class PersonName:
    """Represents a person's name"""

    # Instance Variables
    first_name = ""
    middle_name = ""
    last_name = ""
    
    def __init__(self, first_name, middle_name, last_name):
        """Constructor to initialize the PersonName object"""
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
  
    # Other methods for getting, setting and printing the name