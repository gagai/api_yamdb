from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'USR'
    MODERATOR = 'MDR'
    ADMIN = 'ADM'
    USER_ROLE_CHOICES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]

    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=3,
        choices=USER_ROLE_CHOICES,
        default=USER
    )

    def is_user(self):
        return self.role == self.USER or self.MODERATOR or self.ADMIN

    def is_moderator(self):
        return self.role == self.MODERATOR or self.ADMIN

    def is_admin(self):
        return self.role == self.ADMIN
