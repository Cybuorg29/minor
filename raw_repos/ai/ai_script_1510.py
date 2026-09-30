class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_details(self):
        return self.name + ": " + str(self.marks)