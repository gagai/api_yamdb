from django.shortcuts import render
from rest_framework import viewsets

from reviews.models import User, Category, Genre, Title, Review, Comment
# from .permissions import IsAuthorOrReadOnly
from .serializers import (
    UserSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # делает Влад


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # делает Кирилл


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # делает Кирилл
