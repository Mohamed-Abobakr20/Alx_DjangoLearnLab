from .models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = author.books.all()
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# Query 2: List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

# Query 3: Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")