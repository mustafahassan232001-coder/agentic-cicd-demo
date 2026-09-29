import pytest
from library_system import Book, Library

def test_add_book():
    library = Library()
    book = Book("The Great Gatsby")
    library.add_book(book)
    assert "The Great Gatsby" in library.list_books()

def test_remove_book():
    library = Library()
    library.add_book(Book("1984"))
    library.add_book(Book("Brave New World"))
    library.remove_book("1984")
    assert "1984" not in library.list_books()
    assert "Brave New World" in library.list_books()

def test_list_books():
    library = Library()
    library.add_book(Book("Book A"))
    library.add_book(Book("Book B"))
    assert library.list_books() == ["Book A", "Book B"]