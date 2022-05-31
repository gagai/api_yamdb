from rest_framework import serializers

from reviews.models import User, Category, Genre, Title, Review, Comment


class UserSerializer(serializers.ModelSerializer):
    pass


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'review_id', 'text', 'author', 'pub_date')
        model = Comment
