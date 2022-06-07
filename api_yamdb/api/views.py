from rest_framework import viewsets, filters, status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    action
)
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

from .mixins import ListCreateDestroyViewSet
from .filters import TitleFilter
from .permissions import ReadOnly, IsAuthor, IsModerator, IsAdmin
from reviews.models import User, Category, Genre, Title, Review
from api.serializers import (
    UserSerializer,
    UserSignUpSerializer,
    UserEditSerializer,
    TokenSerializer,
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    ReadOnlyTitleSerializer,
    ReviewSerializer,
    CommentSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    lookup_field = "username"

    @action(
        methods=["get", "patch"],
        detail=False,
        url_path="me",
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=UserEditSerializer,
    )
    def users_own_profile(self, request):
        user = request.user
        if request.method == "GET":
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == "PATCH":
            serializer = self.get_serializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST', ])
@permission_classes([permissions.AllowAny, ])
def sign_up(request):
    serializer = UserSignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user = get_object_or_404(
        User,
        username=serializer.validated_data["username"]
    )
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject="YaMDb registration",
        message=f"Your confirmation code: {confirmation_code}",
        from_email=None,
        recipient_list=[user.email],
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([permissions.AllowAny, ])
def get_jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    if default_token_generator.check_token(
        user, serializer.validated_data['confirmation_code']
    ):
        token = AccessToken.for_user(user)
        return Response({'token': str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnly | IsAdmin]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = "slug"


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [ReadOnly | IsAdmin]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = "slug"


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [ReadOnly | IsAdmin]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ("retrieve", "list"):
            return ReadOnlyTitleSerializer
        return TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [ReadOnly | IsAuthor | IsModerator]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Review, title_id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [ReadOnly | IsAuthor | IsModerator]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        title = get_object_or_404(Review, title_id=title_id)
        review = get_object_or_404(title, review_id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
