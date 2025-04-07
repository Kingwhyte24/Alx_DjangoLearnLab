🚀 Endpoints Overview
Method	Endpoint	Description	Auth Required
GET	/api/books/	List all books	❌ No
GET	/api/books/<id>/	Retrieve a single book by ID	❌ No
POST	/api/books/create/	Create a new book	✅ Yes
PUT	/api/books/<id>/update/	Update an existing book	✅ Yes
DELETE	/api/books/<id>/delete/	Delete a book	✅ Yes


🛠️ Setup Instructions
1. Run the development server

python manage.py runserver
🔐 Authentication
Token-based authentication is recommended.

Add 'rest_framework.authtoken' to INSTALLED_APPS.

Run: python manage.py drf_create_token <username> to get a token.

Include token in headers for POST, PUT, DELETE:


🧩 API Views Summary
📖 BookListView (ListAPIView)
Returns a list of all books.
permission_classes = [AllowAny]


🔍 BookDetailView (RetrieveAPIView)
Returns details of a single book by ID.
permission_classes = [AllowAny]


➕ BookCreateView (CreateAPIView)
Allows authenticated users to create new books.
permission_classes = [IsAuthenticated]


✏️ BookUpdateView (UpdateAPIView)
Allows authenticated users to update a book.
permission_classes = [IsAuthenticated]


🗑️ BookDeleteView (DestroyAPIView)
Allows authenticated users to delete a book.
permission_classes = [IsAuthenticated]




📄 Notes
Ensure that authors exist before creating books (FK dependency).

BookSerializer includes validation: publication_year must not be in the future.

Only authenticated users can create/update/delete.

