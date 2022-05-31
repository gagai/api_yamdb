from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet, TitleViewSet, CategoryViewSet, GenreViewSet,
                    ReviewViewSet, CommentViewSet)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register()  # для reviews делает Кирилл
router.register()  # для comments делает Кирилл

urlpatterns = [
    path('v1/', include(router.urls)),
]
