class Employee: 
    def __init__(self, name, experience, salary):
        self.name = name
        self.experience = experience
        self.salary = salary
        
    def get_name(self):
        return self.name
    
    def get_experience(self):
        return self.experience
    
    def get_salary(self):
        return self.salary