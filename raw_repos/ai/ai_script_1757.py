class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_year(self):
        return self.year
    
    def set_title(self, new_title):
        self.title = new_title
        
    def set_author(self, new_author):
        self.author = new_author
        
    def set_year(self, new_year):
        self.year = new_year