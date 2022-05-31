from rest_framework import serializers

from reviews.models import Review, Comments

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'review_id', 'text', 'author', 'pub_date')