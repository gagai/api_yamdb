from rest_framework import viewsets
from django.shortcuts import get_object_or_404
 
from reviews.models import User, Category, Genre, Title, Review, Comment
# from .permissions import IsAuthorOrReadOnly
from api.serializers import (
    UserSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentsSerializer
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

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Review, title_id=title_id)
        return title.reviews.all() 


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        title = get_object_or_404(Review, title_id=title_id)
        review = get_object_or_404(title, review_id=review_id)
        return review.comments.all()
