class Book:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def list_books(self):
        return [book.title for book in self.books]