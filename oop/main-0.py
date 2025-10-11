from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create book instances
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    ebook1 = EBook("Digital Fortress", "Dan Brown", 5)
    printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 277)

    # Add books to the library (composition)
    my_library.add_book(book1)
    my_library.add_book(ebook1)
    my_library.add_book(printbook1)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
