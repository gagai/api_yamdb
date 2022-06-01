from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet, TitleViewSet, CategoryViewSet, GenreViewSet,
                    ReviewViewSet, CommentsViewSet)
app_name = 'api'

router = DefaultRouter()
#router.register(r"users", UserViewSet)
#router.register(r'titles', TitleViewSet)
#router.register(r'categories', CategoryViewSet)
#router.register(r'genres', GenreViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments/',
    CommentsViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
]
