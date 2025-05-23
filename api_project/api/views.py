# from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework import generics, viewsets
# from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookList(generics.ListAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer
    # serializer = BookSerializer(books, many=True)
    # return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset= Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    # serializer = BookSerializer(books, many=True)
    # return Response(serializer.data)