from rest_framework import permissions


class IsAnonymous(permissions.BasePermission):
    """Только аноним"""

    def has_permission(self, request, view):
        return request.user.is_anonymous


class ReadOnly(permissions.BasePermission):
    """
    Возвращает результат проверки методов HTTP запросов

    True если 'GET', 'HEAD', 'OPTIONS'.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class IsAuthor(permissions.BasePermission):
    """Разрешение для редактирования если пользователь является автором отзыва."""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_client

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.author == request.user


class IsAdministrator(permissions.BasePermission):
    """Возвращает True если пользователь является администратором."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_administrator
