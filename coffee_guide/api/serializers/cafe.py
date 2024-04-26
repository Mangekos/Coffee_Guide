from django.shortcuts import get_object_or_404
from api.utils import Base64ImageField

from users.serializers import CustomUserSerializer

from cafe.models import (
    Alternative,
    Cafe,
    DrinkInCafe,
    Schedule,
    Roaster,
    ScheduleInCafe,
    Additionals,
    Drink,
    Address,
    Available
)
from rest_framework import serializers


class DrinkSerializer(serializers.ModelSerializer):
    """Сериализация данных: Напитков."""

    class Meta:
        model = Drink
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    """Сериализация данных: Время работы."""

    class Meta:
        model = Schedule
        fields = "__all__"


class AdditionalSerializer(serializers.ModelSerializer):
    """Сериализация данных: Тэгов."""

    class Meta:
        model = Additionals
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    """Сериализация данных: Адрес."""

    class Meta:
        model = Address
        fields = "__all__"


class AlternativeSerializer(serializers.ModelSerializer):
    """Сериализация данных: Доп.опции."""
    class Meta:
        model = Alternative
        fields = "__all__"


class AvailableSerializer(serializers.ModelSerializer):
    """Сериализация данных: Доп.опции."""
    class Meta:
        model = Available
        fields = "__all__"


class RoasterSerializer(serializers.ModelSerializer):
    """Сериализация данных: Обжарщиков."""

    class Meta:
        model = Roaster
        fields = "__all__"


class DrinkInCafeGetSerializer(serializers.ModelSerializer):
    """Сериализация данных: Напитки в кофейне get."""
    id = serializers.ReadOnlyField(source="drink.id")
    name = serializers.CharField(source="drink.name")

    class Meta:
        model = DrinkInCafe
        fields = ("id", "name", "cost")


class DrinkInCafeCreateSerializer(serializers.ModelSerializer):
    """Сериализация данных: Напитки в кофейне post."""
    id = serializers.PrimaryKeyRelatedField(
        source="drink",
        queryset=Drink.objects.all()
    )

    class Meta:
        model = DrinkInCafe
        fields = ("id", "cost")


class ScheduleInCafeGetSerializer(serializers.ModelSerializer):
    """Сериализация данных: Расписание в кофейне get."""
    id = serializers.ReadOnlyField(source="schedules.id")
    name = serializers.CharField(source="schedules.name")

    class Meta:
        model = ScheduleInCafe
        fields = ("id", "name", "start", "end")


class ScheduleInCafeCreateSerializer(serializers.ModelSerializer):
    """Сериализация данных: Расписание в кофейне post."""
    id = serializers.PrimaryKeyRelatedField(
        source="shedules",
        queryset=Schedule.objects.all()
    )

    class Meta:
        model = ScheduleInCafe
        fields = ("id", "start", "end")

# class ImageCafeSerializer(serializers.ModelSerializer):
#     """Сериализация данных: Картинок."""

#     class Meta:
#         model = ImageCafe
#         fields = ("image_url", )


class CafeGetSerializer(serializers.ModelSerializer):
    "Гет сериализатор кофеен"
    schedules = ScheduleInCafeGetSerializer(many=True, read_only=True, source="schedule_in_cafe")
    alternatives = AlternativeSerializer(many=True, read_only=True)
    is_alternatives = serializers.BooleanField(read_only=True)
    additionals = AdditionalSerializer(many=True, read_only=True)
    availables = AvailableSerializer(many=True, read_only=True)
    roasters = RoasterSerializer(many=True, read_only=True)
    drinks = DrinkInCafeGetSerializer(many=True, read_only=True, source="drink_in_cafe")
    organization = CustomUserSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    image = Base64ImageField()

    class Meta:
        model = Cafe
        fields = (
            "id",
            "name",
            "description",
            "schedules",
            "alternatives",
            "address",
            "roasters",
            "additionals",
            "availables",
            "is_alternatives",
            "drinks",
            "image",
            "organization"
        )


class CafeCreateSerializer(serializers.ModelSerializer):
    """Пост сериализатор кофеен"""
    schedules = ScheduleInCafeCreateSerializer(many=True)
    drinks = DrinkInCafeCreateSerializer(many=True)
    # address = AddressSerializer()
    roasters = RoasterSerializer(many=True, read_only=True)
    image = Base64ImageField()

    class Meta:
        model = Cafe
        fields = (
            "id",
            "name",
            "description",
            "schedules",
            "alternatives",
            "address",
            "roasters",
            "additionals",
            "availables",
            "is_alternatives",
            "drinks",
            "image",
        )

    def create_drinks(
            self,
            drinks,
            instance,
    ):
        DrinkInCafe.objects.bulk_create(
            [
                DrinkInCafe(
                    cafe=instance,
                    drink=get_object_or_404(
                        Drink, id=drink_data["drink"].id
                    ),
                    cost=drink_data["cost"]
                )
                for drink_data in drinks
            ]
        )

    def create_schedules(
            self,
            schedules,
            instance,
    ):
        ScheduleInCafe.objects.bulk_create(
            [
                ScheduleInCafe(
                    cafe=instance,
                    schedules=get_object_or_404(
                        Schedule, id=schedules_data["shedules"].id
                    ),
                    start=schedules_data["start"],
                    end=schedules_data["end"]
                )
                for schedules_data in schedules
            ]
        )

    def create(self, validated_data):
        schedules = validated_data.pop("schedules")
        drinks = validated_data.pop("drinks")
        instance = super().create(validated_data)
        self.create_schedules(schedules, instance)
        self.create_drinks(drinks, instance)
        return instance

    def update(self, instance, validated_data):
        schedules = validated_data.pop("schedules")
        drinks = validated_data.pop("drinks")
        instance.schedules.clear()
        instance.drinks.clear()
        super().update(instance, validated_data)
        self.create_schedules(schedules, instance)
        self.create_drinks(drinks, instance)
        instance.save()
        return instance

    def to_representation(self, instance):
        request = self.context.get("request")
        context = {"request": request}
        return CafeGetSerializer(instance, context=context).data
