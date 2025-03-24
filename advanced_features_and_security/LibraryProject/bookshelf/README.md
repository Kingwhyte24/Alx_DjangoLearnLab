# Role-Based Access Control in Django

## Overview
This Django application implements role-based access control (RBAC) using **custom permissions** and **groups** to manage access to book-related actions such as viewing, creating, editing, and deleting books.

---
## 1️⃣ Custom Permissions

We define four custom permissions within the `Book` model:
- `can_view` → Allows users to view books.
- `can_create` → Allows users to add new books.
- `can_edit` → Allows users to edit existing books.
- `can_delete` → Allows users to delete books.

### 📌 Implementation (models.py)
```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]
```

---
## 2️⃣ Groups & Permissions
Django groups are used to assign permissions to users in a structured manner.

### 🏷️ Groups Created:
- **Viewers** → Only have `can_view` permission.
- **Editors** → Have `can_view`, `can_create`, and `can_edit` permissions.
- **Admins** → Have all permissions, including `can_delete`.

### 📌 Automatic Group Creation (signals.py)
To automate the creation of groups and their permissions when the app runs:
```python
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.apps import apps
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'relationship_app':  # Change to your app name
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in permissions:
                permission = Permission.objects.filter(codename=perm).first()
                if permission:
                    group.permissions.add(permission)
```

This ensures groups are **created automatically** after migrations.

---
## 3️⃣ Enforcing Permissions in Views
Django’s `@permission_required` decorator is used to enforce permissions.

### 📌 Example Implementation (views.py)
```python
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'delete_success.html')
```

**🔹 How it Works:**
- If a user **does not have the required permission**, a **403 Forbidden** error is raised.
- Only **authorized users** can access each view based on their role.

---
## 4️⃣ URL Configuration

To properly route the secured views, define URLs in `urls.py`:
```python
from django.urls import path
from .views import book_list, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]
```

---
## 5️⃣ Testing the Setup
1. **Create users** using:
   ```sh
   python manage.py createsuperuser
   ```
2. **Log in to Django Admin (`/admin`)**
3. **Create test users and assign them to groups** (`Viewers`, `Editors`, `Admins`).
4. **Log in as each test user** and try accessing different pages.
5. **Verify if permissions work correctly** (e.g., Editors shouldn't be able to delete books).

---
## Summary ✅
✔ **Custom permissions** (`can_view`, `can_create`, `can_edit`, `can_delete`) added to `Book` model.
✔ **User groups** (`Viewers`, `Editors`, `Admins`) manage access levels.
✔ **Permissions enforced** in views using `@permission_required`.
✔ **Automatic group creation** using Django signals.
✔ **URL patterns** configured to route secured views.
✔ **Test users and groups verified** for correct access control.

🎉 **Your Django app now has fully functional Role-Based Access Control!** 🚀

