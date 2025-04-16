from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/', views.PostCreateView.as_view(), name='post-detail'),
    path('posts/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/', views.PostDeleteView.as_view(), name='post-delete'),

]