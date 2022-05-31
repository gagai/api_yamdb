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
        Genre, on_delete=models.SET_NULL,
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
    pass
    # делает Кирилл


class Comment(models.Model):
    """Комментарии к отзывам (Review)"""
    pass
    # делает Кирилл
