from api.utils import password_generation
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from coffee_guide.settings import EMAIL_HOST_USER

from .models import CustomUser
from .serializers import ResetPasswordSerializer
from drf_spectacular.utils import (
    # OpenApiParameter,
    extend_schema,
    extend_schema_view,
)


@extend_schema(
    tags=["Организация"],
    methods=["GET", "POST", "DELETE"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список организаций",
    ),
    retrieve=extend_schema(
        summary="Детальная информация об организации",
    ),
    create=extend_schema(
        summary="Создание организации",
    ),
    destroy=extend_schema(
        summary="Удаление организации",
    ),
)
class CustomUserViewSet(UserViewSet):
    """
    Вьюсет для:

    - изменения пароля;
    - регистрации нового пользователя;
    """

    # @extend_schema(summary="Отправка пароля на почту при регистрации")
    # def perform_create(self, serializer, *args, **kwargs):
    #     """Отправка пароля на почту при регистрации."""
    #     user = serializer.save()

    #     password = password_generation()
    #     user.set_password(make_password(password))
    #     user.save()

    #     send_mail(
    #         "Пароль",
    #         f"Ваш пароль: {password}",
    #         EMAIL_HOST_USER,
    #         [user.email],
    #         fail_silently=False,
    #     )

    @extend_schema(summary="Отправка пароля на почту при изменении пароля")
    @action(["post"], detail=False)
    def reset_password(self, request, *args, **kwargs):
        """Отправка пароля на почту при изменении пароля."""
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = CustomUser.objects.get(email=serializer.data["email"])
        new_password = password_generation()
        user.password = make_password(new_password)
        user.save()

        send_mail(
            "Новый пароль",
            f"Ваш новый пароль: {new_password}",
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
