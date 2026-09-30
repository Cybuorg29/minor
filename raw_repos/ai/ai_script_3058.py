class Book:
    def __init__(self, title, author, publisher, pages):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
   
    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publisher: {self.publisher}")
        print(f"Pages: {self.pages}")