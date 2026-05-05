class Book:
    def __init__(self,title,author,copies):
        self.title = title
        self.author = author
        self.copies = copies
    def display(self):
        return f'title: {self.title}\nauthor: {self.author}\ncopies: {self.copies}'


#Object Creation
book1 = Book("SQA","Test",10)
print("Book 2 Information =",book1.display())
title = input("Enter your title: ")
author = input("Enter your author: ")
copies = input("Enter your copies: ")
book2 = Book(title,author,copies)
print("Book 2 Information =",book2.display())