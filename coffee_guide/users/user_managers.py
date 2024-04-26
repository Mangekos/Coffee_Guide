from django.contrib.auth.models import BaseUserManager

from .gmail_utils import send_email
from api.utils import password_generation
from coffee_guide.settings import DEFAULT_USER_NAME, EMAIL_HOST_USER


text = "Ваш пароль: {password}.\n\n Никому не передавайте свой пароль в целях безопасности!"


class CustomUserManager(BaseUserManager):
    """Менеджер модели пользователя, для регистрации с ИНН."""

    use_in_migrations = True

    def create_user(
        self,
        email,
        organization_inn,
        password=None,
        username=None,
        name=DEFAULT_USER_NAME,
        **extra_fields,
    ):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        if username is None:
            username = organization_inn

        user = self.model(
            username=username,
            password=password,
            organization_inn=organization_inn,
            email=email,
            name=name,
        )
        if password is None:
            password = password_generation()
            send_email(
                subject="Пароль",
                message=f"Ваш пароль: {password}\n\n",
                # "Никому не передавайте свой пароль в целях безопасности!",
                sender=EMAIL_HOST_USER,
                to=[user.email],
                # fail_silently=False,
            )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, password, organization_inn=None, **extra_fields
    ):
        if organization_inn is None:
            organization_inn = password_generation()

        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Суперпользователь должен быть is_superuser=True."
            )

        user = self.create_user(
            username=username,
            password=password,
            organization_inn=organization_inn,
            **extra_fields,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
