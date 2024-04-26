import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.getenv("SECRET_KEY", default=get_random_secret_key())

# DEBUG = os.getenv('DEBUG', 'True') == 'True'
DEBUG = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1").split(" ")


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "api.apps.ApiConfig",
    "cafe.apps.CafeConfig",
    "users.apps.UsersConfig",
    "djoser",
    "social_django",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

# CORS_ORIGIN_WHITELIST = [
#     "http://coffee-gid.ddns.net",
#     "https://coffee-gid.ddns.net",
#     "http://localhost:8000",
#     "http://127.0.0.1:8000",
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
#     "http://localhost:8000/api/v1",
#     "http://127.0.0.1:8000/api/v1/cafes?page=1"
# ]

CORS_ALLOW_ALL_ORIGINS = True

CORS_URLS_REGEX = r"^/api/v1/.*$"


ROOT_URLCONF = "coffee_guide.urls"

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "coffee_guide.wsgi.application"


# DATABASES = {
#     "default": {
#         "ENGINE": os.getenv(
#             "DB_ENGINE", default="django.db.backends.postgresql"
#         ),
#         "NAME": os.getenv("POSTGRES_DB"),
#         "USER": os.getenv("POSTGRES_USER"),
#         "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
#         "HOST": os.getenv("DB_HOST"),
#         "PORT": os.getenv("DB_PORT"),
#     }
# }

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.getenv(
                "DB_ENGINE", default="django.db.backends.postgresql"
            ),
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.CustomUser"
TOKEN_MODEL = "users.CustomUser"
# AUTHENTICATION_BACKENDS = ("users.backends.AuthBackend",)

# SOCIAL_AUTH_USER_MODEL = "users.CustomUser"
# SOCIAL_AUTH_URL_NAMESPACE = 'social'

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication"
    ],
    # "SEARCH_PARAM": "name",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# SIMPLE_JWT = {
#     'AUTH_HEADER_TYPES': ('JWT',),
# }

SPECTACULAR_SETTINGS = {
    "TITLE": "Coffee_guide",
    "DESCRIPTION": "Coffee Guide for human",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

DJOSER = {
    # "SEND_ACTIVATION_EMAIL": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    # "TOKEN_MODEL": None,
    # "ACTIVATION_URL": "api/v1/users/activation/{uid}/{token}/",
    "HIDE_USERS": False,
    "LOGIN_FIELD": "username",
    "SERIALIZERS": {
        "user_create": "users.serializers.OnlyInnCreateUserSerializer",
        "user": "users.serializers.CustomUserSerializer",
        "current_user": "users.serializers.CustomUserSerializer",
    },
    "PERMISSIONS": {
        "user": ["rest_framework.permissions.AllowAny"],
        "user_list": ["rest_framework.permissions.AllowAny"],
    },
    # "EMAIL": {
    #     # "activation": "users.views.ActivationEmail",
    #     "password_reset": "users.views.PasswordResetEmail"
    # },
}

AUTHENTICATION_BACKENDS = (
    "social_core.backends.vk.VKOAuth2",
    "social_core.backends.github.GithubOAuth2",
    # "django.contrib.auth.backends.ModelBackend",
    'users.backends.AuthBackend'
)

SOCIAL_AUTH_VK_OAUTH2_KEY = "51814626"
SOCIAL_AUTH_VK_OAUTH2_SECRET = "jaxoNQgoU2BPn58SfmWh"

SOCIAL_AUTH_GITHUB_KEY = "Iv1.de0e9327a12e1c62"
SOCIAL_AUTH_GITHUB_SECRET = "8370cc6cf8f426021bdc65f1491d60032669860c"

SOCIAL_AUTH_VK_OAUTH2_SCOPE = ["email"]
SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "users.pipelines.save_user_github",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)

LOGIN_REDIRECT_URL = "/api/v1/cafe/"

# smtp
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "coffeegyd@gmail.com"
EMAIL_HOST_PASSWORD = "whip ramt iide mmxm"

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True
USE_L10N = True
USE_TZ = False


STATIC_URL = "/static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_ROOT = BASE_DIR / 'collected_static'

MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DEFAULT_USER_NAME = "Гость"


TOKEN = os.getenv("DADATA_TOKEN_KEY")
SECRET = os.getenv("DADATA_SECRET_KEY")


CHARS = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@mail.ru")
