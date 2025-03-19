from django.urls import path
from .views import list_books, LibraryDetailView, register, user_login, user_logout
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view
    path("register/", register, name="register"),
    # path("register/", views.register, name="register"),

    # Login and Logout using Django's built-in views
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('admin-view/', views.Admin, name='Admin'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete/<int:book_id>/", views.delete_book, name="delete_book"),
]
