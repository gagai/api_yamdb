from rest_framework import serializers

from reviews.models import User, Category, Genre, Title, Review, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    rating = serializers.SerializerMethodField()
=======
>>>>>>> 431c78272e2dbdba97b717d67d733710ac0a1b88

    class Meta:
        fields = '__all__'
        model = Title

    def get_rating(self, obj):
        scores = Review.objects.filter(title_id=obj.id)
        return sum(scores) / len(scores)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'review_id', 'text', 'author', 'pub_date')
        model = Comment
