#!/usr/bin/env python3


    class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

# Example usage:
my_book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", pages=218)

# Display information about the book
print(my_book.display_info())
        