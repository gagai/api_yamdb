from django.core.management.base import BaseCommand, CommandError
from users.models import User
from reviews.models import Category, Comment, GenreTitle, Genre, Review, Title
from api_yamdb.settings import BASE_DIR
import csv

file_model_dict = {
    'users.csv' : User,
    'category.csv' : Category,
    'genre.csv' : Genre,
    'titles.csv' : Title,
    'genre_title.csv' : GenreTitle,
    'review.csv' : Review,
    'comments.csv' : Comment,
}
path = BASE_DIR + '/static/data/'


class Command(BaseCommand):
    help = 'Загружает тестовые данные в базу данных'

    def handle(self, *args, **options):
        for file, model in file_model_dict.items():
            with open(f'{path}{file}') as file:
                reader = csv.DictReader(file, delimiter=',')
                for data in reader:
                    model.objects.create(**data)
