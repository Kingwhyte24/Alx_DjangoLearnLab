from bookshelf.models import Book
book = Book.objects.all()
print(book)

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
