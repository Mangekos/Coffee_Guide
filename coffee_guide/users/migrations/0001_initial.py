import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import users.user_managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                ("name", models.CharField(max_length=70, verbose_name="ФИО")),
                ("username", models.CharField(default="username", max_length=50, unique=True, verbose_name="Юзернейм")),
                (
                    "organization_inn",
                    models.CharField(
                        max_length=12,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(10)],
                        verbose_name="ИНН организации",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True, verbose_name="Почта")),
                ("password", models.CharField(max_length=128, verbose_name="Пароль")),
                ("is_verified", models.BooleanField(default=False, verbose_name="Проверка верификации")),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
                "ordering": ("email",),
            },
            managers=[
                ("objects", users.user_managers.CustomUserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name="customuser",
            constraint=models.UniqueConstraint(
                fields=("organization_inn", "email"), name="organization_inn_email_unique"
            ),
        ),
    ]
