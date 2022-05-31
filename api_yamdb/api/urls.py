from django.urls import include, path
<<<<<<< HEAD
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
=======
from api.views import CommentsViewSet, ReviewViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews/', ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments/',
                CommentsViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls))
>>>>>>> dev
]
