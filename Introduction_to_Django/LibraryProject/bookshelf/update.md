from bookshelf.models import Book
update_title = Book.objects.filter(title='1984').update(title='Nineteen Eighty-Four')

#Nineteen Eighty-Four by George Orwell (1949)