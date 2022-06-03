from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from .mixins import ListCreateDestroyViewSet
<<<<<<< HEAD
from .permissions import IsAdminOrReadOnly, IsAdmin, IsAuthor, IsModerator
=======
from .permissions import ReadOnly, IsAuthor, IsModerator, IsAdmin
>>>>>>> 8167fc7ae7c0d781bf948f9286a7a84612be407e
from reviews.models import User, Category, Genre, Title, Review
from api.serializers import (
    UserSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # делает Влад


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnly|IsAdmin]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [ReadOnly|IsAdmin]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [ReadOnly|IsAdmin]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year')


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
<<<<<<< HEAD
    permission_classes = (IsAdmin, IsModerator, IsAuthor)
=======
    permission_classes = [ReadOnly|IsAuthor|IsModerator]
>>>>>>> 8167fc7ae7c0d781bf948f9286a7a84612be407e

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Review, title_id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
<<<<<<< HEAD
    permission_classes = (IsAdmin, IsModerator, IsAuthor)
=======
    permission_classes = [ReadOnly|IsAuthor|IsModerator]
>>>>>>> 8167fc7ae7c0d781bf948f9286a7a84612be407e

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        title = get_object_or_404(Review, title_id=title_id)
        review = get_object_or_404(title, review_id=review_id)
        return review.comment.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
