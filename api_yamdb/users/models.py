from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
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
        max_length=30,
        verbose_name='Роль',
        choices=USER_ROLE_CHOICES,
        default=USER,
        blank=False
    )

    def is_user(self):
        return self.role == self.USER or self.MODERATOR or self.ADMIN

    def is_moderator(self):
        return self.role == self.MODERATOR

    def is_admin(self):
        return self.role == self.ADMIN
