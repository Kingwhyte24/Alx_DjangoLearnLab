from django.shortcuts import render
from .models import Book, Library
from .models import Library
from django.views.generic import DetailView

# Create your views here.
# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-Based View: Show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"