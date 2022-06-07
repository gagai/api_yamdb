from django.core.management.base import BaseCommand, CommandError
from reviews.models import Title, Genre, Category, Review, Comment
from api_yamdb.settings import BASE_DIR
import csv

class Command(BaseCommand):
    help = 'Загружает тестовые данные в базу данных'

    def handle(self, *args, **options):
        path = BASE_DIR + '/static/data/'
        files_list = [
            'category.csv',
            'comments.csv',
            'genre_title.csv',
            'genre.csv',
            'review.csv',
            'titles.csv',
            'users.csv',
        ]

        for file in files_list:
            with open(f'{path}{file}') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)