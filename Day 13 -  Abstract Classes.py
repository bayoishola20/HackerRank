#==================== GIVEN ======================#
from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
#===================== END =========================#

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self,title,author)
        self.price = price
    def display(self):
        print "Title: " + self.title + "\n" + "Author: " + self.author + "\n" + "Price: " + str(self.price)


#==================== GIVEN ======================#
title=raw_input()
author=raw_input()
price=int(raw_input())
new_novel=MyBook(title,author,price)
new_novel.display()
#===================== END =========================#