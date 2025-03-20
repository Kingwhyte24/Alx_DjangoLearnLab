from django.contrib import admin

# Register your models here.
from .models import Author, Book, Library, Librarian
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Customize Admin Panel for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "date_of_birth", "profile_photo"),
        }),
    )
    search_fields = ("username", "email")
    ordering = ("username",)

admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
