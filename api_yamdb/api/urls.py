from django.db import router
from django.urls import include, path
from api.views import CommentsViewSet, ReviewViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews/', ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments/',
                CommentsViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls))
]
