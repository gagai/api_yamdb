from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Пользователи и их роли"""
    pass
    # делает Влад


class Category(models.Model):
    """Категории (типы: фильм, книга или песенка) произведений"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    """Категории жанров"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Title(models.Model):
    """Произведения, к которым пишут отзывы
    (определённый фильм, книга или песенка)"""
    name = models.TextField()
    year = models.IntegerField()
    сategory = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name="сategory", blank=True, null=True
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="genres", blank=True, null=True
    )
    rating = models.IntegerField(
        null=True,
        default=None
    )

    def __str__(self):
        return self.text


class Review(models.Model):
    """Отзывы на произведения (Title)"""
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_author'
    )
    score = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    """Комментарии к отзывам (Review)"""
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments_author'
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:15]
