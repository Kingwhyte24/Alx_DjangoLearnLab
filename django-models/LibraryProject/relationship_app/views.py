from django.shortcuts import render, redirect
from .models import Book, Library
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test

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

def register(request):
    if request.method == "POST":
        forms = UserCreationForm(request.POST)
        if forms.is_valid:
            user = forms.save
            login(request, user)
            return redirect("list_books")

    else:
        form = UserCreationForm()
        return render(request, "relationship_app/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
        return render(request, "relationship_app/login.html", {"form": form})
    

def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == "Admin"

def is_librarian(user):
    hasattr(user, 'userprofile') and user.userprofile.role == "Liberarian"

def is_member(user):
    hasattr(user, 'userprofile') and user.userprofile.role = "Member"

@user_passes_test(is_admin)
def Admin_view(request):
    return render('ADMIN VIEW')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render('Librarian view')

@user_passes_test(is_member)
def member_view(request):
    return render('Member View')