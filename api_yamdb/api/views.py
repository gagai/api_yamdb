from rest_framework import viewsets, filters, status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from .mixins import ListCreateDestroyViewSet
from .permissions import ReadOnly, IsAuthor, IsModerator, IsAdmin
from reviews.models import User, Category, Genre, Title, Review
from api.serializers import (
    UserSerializer,
    UserSignUpSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentSerializer
)
from .utils import get_confirmation_code


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # делает Влад


@api_view(['POST',])
@authentication_classes([])
@permission_classes([AllowAny,])
def sign_up(request):
    if request.method == 'POST':
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            if username == 'me':
                return Response(
                    serializer.data, status=status.HTTP_400_BAD_REQUEST
                )
            email = serializer.validated_data.get('email')
            confirmation_code = get_confirmation_code()
            text_message = f'{username}, вот твой {confirmation_code}'
            send_mail(
                recipient_list = [email,],
                subject=f'Проверочный код для пользователя {username}',
                message=text_message,
                from_email=None,
            )
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    filterset_fields = ('name', 'year')


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [ReadOnly|IsAuthor|IsModerator]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Review, title_id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [ReadOnly|IsAuthor|IsModerator]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        title = get_object_or_404(Review, title_id=title_id)
        review = get_object_or_404(title, review_id=review_id)
        return review.comment.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
