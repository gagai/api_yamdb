from django.db import models

from users.models import User
from api.validators import validate_year


CHOICES = ((1, 1),
           (2, 2),
           (3, 3),
           (4, 4),
           (5, 5),
           (6, 6),
           (7, 7),
           (8, 8),
           (9, 9),
           (10, 10))


class Category(models.Model):
    """Категории (типы: фильм, книга или песенка) произведений"""
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Категории жанров"""
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    """Произведения, к которым пишут отзывы
    (определённый фильм, книга или песенка)"""
    name = models.CharField(max_length=256)
    year = models.IntegerField(validators=[validate_year])
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="titles",
        null=True,
    )
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(
        Genre,
        related_name="titles",
        through='TitleGenre',
    )
    rating = models.FloatField(
        null=True,
        default=None
    )

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    """Вспомогательная таблица"""
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.genre}'


class Review(models.Model):

    """Отзывы на произведения (Title)"""
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_author')
    score = models.IntegerField(choices=CHOICES)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    """Комментарии к отзывам (Review)"""
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments_author')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:15]
