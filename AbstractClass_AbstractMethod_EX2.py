#Library Management System: Create a Python class hierarchy for a library management system. There should be a base class LibraryItem with subclasses Book and DVD.
#Each library item should have attributes such as title, author/director, genre, and availability status.
#Implement methods for checking out, returning, and displaying information about library items.
#Ensure that the system can handle multiple copies of the same item and track their availability correctly.

from abc import ABC,abstractmethod


class LibraryItem(ABC):
    @abstractmethod
    def __init__(self,title, author, genre, availability_status):
        self.title = title
        self.author = author
        self. genre = genre
        self.availability_status = availability_status
        pass

    
class Book(LibraryItem):
    def __init__(self, title, author, genre, availability_status, ISBN, pages, publication_year):
        super().__init__(title, author, genre, availability_status)
        self.ISBN = ISBN
        self.pages = pages
        self.publication_year = publication_year
            
    
    def check_out(self):
        checking_out = int(input("enter the ISBN number: "))
        
        
        #if iter in range(1,200):
        if self.availability_status in range(1,200):
            print("item is returned and available")
        else:
            print("item is not available")
           

    def return_item(self):
        print("item as returned and available")
        
    def display_information(self):
        print(self.title, self.author, self.genre, self.availability_status)



class DVD(LibraryItem):
    def __init__(self, title, author, genre, availability_status, duration, release_year, main_actors):
        super().__init__(title, author, genre, availability_status)
        self.duration = duration
        self.release_year = release_year
        self.main_actors = main_actors


    def check_out(self):
        checking_out = int(input("enter the release_year: "))
        
        
        #if iter in range(1996):
        if self.availability_status in range(1996):
            print("DVD is returned and available")
        else:
            print("DVD is not available")
           

    def return_item(self):
        print("DVD is returned and available")
        
    def display_information(self):
        print(self.title, self.author, self.genre, self.availability_status, self.duration, self.release_year, self.main_actors)



object = Book(title = "python", author = "Guido", genre = "program", availability_status = "Avilable", ISBN = 123, pages = 40, publication_year = 1995)
object.check_out()
object.return_item()
object.display_information()



object_2 = DVD(title = "python", author = "Guido", genre = "program", availability_status = "Avilable", duration = "1hr", release_year = 1996, main_actors = "Guido van Rossum")
object_2.check_out()
object_2.return_item()
object_2.display_information()









