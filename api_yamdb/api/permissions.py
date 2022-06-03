from rest_framework import permissions

from reviews import models
from users.models import User


review_model_name = models.Review.__name__
title_model_name = models.Title.__name__
allowed_object_names = (
    review_model_name,
    title_model_name,
)

user_role = User.USER
moderator_role = User.MODERATOR
admin_role = User.ADMIN


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous == True:
            return False
        return (request.user.role == request.user.is_user()
                or request.user.is_superuser
                )

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous == True:
            return False
        return (request.user.role == request.user.is_moderator()
                or request.user.is_superuser
                )

    def has_object_permission(self, request, view, obj):
        return obj.__class__.__name__ in allowed_object_names


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous == True:
            return False
        return (request.user.role == request.user.is_admin()
                or request.user.is_superuser
                )
