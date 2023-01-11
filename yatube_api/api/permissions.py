from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Пользовательские разрешения.
    Не авторизированные пользователи, только просматривают контент авторов
    и оставляют комментарии.
    Авторы постов и комментариев могут редактировать только свои записи.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
