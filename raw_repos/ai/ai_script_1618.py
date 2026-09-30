class StudentGrades:
    def __init__(self, names, grades):
        self.names = names
        self.grades = grades
    
    def add_entry(self, name, grade):
        self.names.append(name)
        self.grades.append(grade)
        
    def get_grade(self, name):
        for i in range(len(self.names)):
            if self.names[i] == name:
               return self.grades[i]