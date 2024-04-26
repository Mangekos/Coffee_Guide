from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from .user_managers import CustomUserManager


class CustomUser(AbstractUser):
    """Модель Пользователя."""

    name = models.CharField(
        "ФИО",
        unique=False,
        max_length=70,
        blank=False,
        null=False,
    )
    username = models.CharField(
        "Юзернейм",
        unique=True,
        max_length=50,
        blank=False,
        null=False,
        default="username"
    )
    organization_inn = models.CharField(
        "ИНН организации",
        unique=True,
        max_length=12,
        blank=False,
        null=False,
        validators=[MinLengthValidator(10)],
    )
    email = models.EmailField(
        "Почта",
        unique=True,
        max_length=254,
        blank=False,
        null=False,
    )
    password = models.CharField(
        "Пароль",
        max_length=128,
        blank=False,
        null=False,
    )
    is_verified = models.BooleanField("Проверка верификации", default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)
        constraints = (
            models.UniqueConstraint(
                fields=("organization_inn", "email"),
                name="organization_inn_email_unique",
            ),
        )

    def __str__(self):
        return f"Почта организации {self.email}, ИНН {self.organization_inn}"
