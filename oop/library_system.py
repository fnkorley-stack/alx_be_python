# library_system.py

class Book:
    """Base class representing a general book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"{self.title} by {self.author} (EBook, {self.file_size}MB)"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} (PrintBook, {self.page_count} pages)"


class Library:
    """Class demonstrating composition by managing a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self):
        """Lists all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
