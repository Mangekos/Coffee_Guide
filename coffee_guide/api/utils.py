import random
import base64

from dadata import Dadata
from rest_framework.serializers import ValidationError

from coffee_guide.settings import CHARS, SECRET, TOKEN

from rest_framework import serializers
from django.core.files.base import ContentFile


def check_inn(organization_inn):
    """Проверка ИНН с помощью сервиса DaData."""
    dadata = Dadata(TOKEN, SECRET)
    result = dadata.find_by_id(name="party", query=organization_inn)
    if not result:
        raise ValidationError("ИНН не существует.")


def password_generation():
    """Генерация пароля."""

    password = ""
    for i in range(9):
        password += random.choice(CHARS)

    return password


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)
        return super().to_internal_value(data)
