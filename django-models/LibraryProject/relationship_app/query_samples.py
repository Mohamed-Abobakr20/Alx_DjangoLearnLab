from .models import Author, Book, Library, Librarian

# Query 1: Books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# Query 2: List all books in a specific library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

# Query 3: Get the librarian of the library
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")