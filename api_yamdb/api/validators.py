import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    now = datetime.datetime.now()
    if now.year < value or value < 1000:
        raise ValidationError(
            "Введите корректное значение year",
            params={"value": value},
        )
