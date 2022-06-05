from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (UserViewSet, TitleViewSet, CategoryViewSet, GenreViewSet,
                    ReviewViewSet, CommentViewSet, sign_up)
app_name = 'api'

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments/',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'
         ),
    path('v1/auth/signup/', sign_up, name='sign_up')
]
