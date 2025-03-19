from django.urls import path
from .views import list_books, LibraryDetailView, register, user_login, user_logout

urlpatterns = [
    path("books/", list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view
    path("login/", user_login, name="user_login"),
    path("register/", register, name="register"),
    path("logout/", user_logout, name="user_logout"),
]
