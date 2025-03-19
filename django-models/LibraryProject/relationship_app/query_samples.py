import django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a specific library (EXACT MATCH)
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # This ensures the exact match
    return librarian

# Sample execution
if __name__ == "__main__":
    print("Books by George Orwell:", list(get_books_by_author("George Orwell")))
    print("Books in Central Library:", list(get_books_in_library("Central Library")))
    print("Librarian of Central Library:", get_librarian_for_library("Central Library"))
