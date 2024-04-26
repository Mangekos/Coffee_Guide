from api.utils import check_inn
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from djoser.serializers import (
    UserCreateSerializer,
    UserSerializer,
)
from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "name",
            "email",
            "organization_inn",
        )


class OnlyInnCreateUserSerializer(UserCreateSerializer):
    """Сериализатор для регистрации."""

    organization_inn = serializers.CharField(
        max_length=12, validators=[MinLengthValidator(10)]
    )
    email = serializers.EmailField(max_length=50)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            # "username",
            "name",
            "email",
            "organization_inn",
        )

    def validate(self, attrs):
        organization_inn = attrs.get("organization_inn")
        try:
            check_inn(organization_inn)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

        return attrs


class ResetPasswordSerializer(serializers.ModelSerializer):
    """Сериализатор для восстановления пароля."""

    email = serializers.EmailField(max_length=50)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
        )
