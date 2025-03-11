from bookshelf.models import Book

update_title = Book.objects.get(title='1984')
update_title.title='Nineteen Eighty-Four'
update_title.save()
print(Book.objects.get(title=update_title.title))

#Nineteen Eighty-Four by George Orwell (1949)