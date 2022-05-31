from django.shortcuts import get_object_or_404
from reviews.models import Review, Comments
from rest_framework import viewsets
from api import serializers 


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Review, title_id=title_id)
        return title.reviews.all() 


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentsSerializer

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        title = get_object_or_404(Review, title_id=title_id)
        review = get_object_or_404(title, review_id=review_id)
        return review.comments.all()
