import json
import os
import io
from PIL import Image
from django.core.files import File
from pathlib import Path

from django.core.management.base import BaseCommand
import requests
from coffee_guide.settings import BASE_DIR, ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_USERNAME
from cafe.models import (
    Cafe,
    Address,
    Schedule,
    Roaster,
    Alternative,
    Additionals,
    Drink,
    Available
)
from users.models import CustomUser


class Command(BaseCommand):
    def import_additinals_from_file(self) -> None:
        data_folder: str = os.path.join(BASE_DIR, "data")
        with open(
            os.path.join(data_folder, 'additionally.json'), encoding="utf-8"
        ) as data_file:
            data: json = json.loads(data_file.read())
            for data_object in data:
                id: int = data_object.get("id", None)
                name: str = data_object.get(
                    "name", None
                )
                slug: str = data_object.get(
                    "slug", None
                )

                try:
                    additinals, created = (
                        Additionals.objects.get_or_create(
                            id=id,
                            name=name,
                            slug=slug,
                        )
                    )
                    if created:
                        additinals.save()
                        display_format = (
                            "\n additinals, {}, has been saved."
                        )
                        print(display_format.format(additinals))
                except Exception as ex:
                    print(str(ex))
                    msg: str = (
                        "\n\nSomething went wrong saving this additinals:"
                        " {}\n{}".format(name, str(ex))
                    )
                    print(msg)

    def import_roasters_from_file(self) -> None:
        data_folder: str = os.path.join(BASE_DIR, "data")
        with open(
            os.path.join(data_folder, 'roaster.json'), encoding="utf-8"
        ) as data_file:
            data: json = json.loads(data_file.read())
            for data_object in data:
                id: int = data_object.get("id", None)
                name: str = data_object.get(
                    "name", None
                )
                slug: str = data_object.get(
                    "slug", None
                )

                try:
                    roaster, created = (
                        Roaster.objects.get_or_create(
                            id=id,
                            name=name,
                            slug=slug,
                        )
                    )
                    if created:
                        roaster.save()
                        display_format = (
                            "\nroaster, {}, has been saved."
                        )
                        print(display_format.format(roaster))
                except Exception as ex:
                    print(str(ex))
                    msg: str = (
                        "\n\nSomething went wrong saving this roaster:"
                        " {}\n{}".format(name, str(ex))
                    )
                    print(msg)

    def import_drinks_from_file(self) -> None:
        data_folder: str = os.path.join(BASE_DIR, "data")
        with open(
            os.path.join(data_folder, 'drink.json'), encoding="utf-8"
        ) as data_file:
            data: json = json.loads(data_file.read())
            for data_object in data:
                id: int = data_object.get("id", None)
                name: str = data_object.get(
                    "name", None
                )
                slug: str = data_object.get(
                    "slug", None
                )

                try:
                    drink, created = (
                        Drink.objects.get_or_create(
                            id=id,
                            name=name,
                            slug=slug,
                        )
                    )
                    if created:
                        drink.save()
                        display_format = (
                            "\n drink, {}, has been saved."
                        )
                        print(display_format.format(drink))
                except Exception as ex:
                    print(str(ex))
                    msg: str = (
                        "\n\nSomething went wrong saving this drink:"
                        " {}\n{}".format(name, str(ex))
                    )
                    print(msg)

    def import_alternatives_from_file(self) -> None:
        data_folder: str = os.path.join(BASE_DIR, "data")
        with open(
            os.path.join(data_folder, 'alternative.json'), encoding="utf-8"
        ) as data_file:
            data: json = json.loads(data_file.read())
            for data_object in data:
                id: int = data_object.get("id", None)
                name: str = data_object.get(
                    "name", None
                )
                slug: str = data_object.get(
                    "slug", None
                )

                try:
                    alternative, created = (
                        Alternative.objects.get_or_create(
                            id=id,
                            name=name,
                            slug=slug,
                        )
                    )
                    if created:
                        alternative.save()
                        display_format = (
                            "\n alternative, {}, has been saved."
                        )
                        print(display_format.format(alternative))
                except Exception as ex:
                    print(str(ex))
                    msg: str = (
                        "\n\nSomething went wrong saving this alternative:"
                        " {}\n{}".format(name, str(ex))
                    )
                    print(msg)

    def import_availables_from_file(self) -> None:
        data_folder: str = os.path.join(BASE_DIR, "data")
        with open(
            os.path.join(data_folder, 'available.json'), encoding="utf-8"
        ) as data_file:
            data: json = json.loads(data_file.read())
            for data_object in data:
                id: int = data_object.get("id", None)
                name: str = data_object.get(
                    "name", None
                )
                slug: str = data_object.get(
                    "slug", None
                )

                try:
                    available, created = (
                        Available.objects.get_or_create(
                            id=id,
                            name=name,
                            slug=slug,
                        )
                    )
                    if created:
                        available.save()
                        display_format = (
                            "\n available, {}, has been saved."
                        )
                        print(display_format.format(available))
                except Exception as ex:
                    print(str(ex))
                    msg: str = (
                        "\n\nSomething went wrong saving this available:"
                        " {}\n{}".format(name, str(ex))
                    )
                    print(msg)

    def import_schedules_from_file(self) -> None:
        data_folder: str = os.path.join(BASE_DIR, "data")
        with open(
            os.path.join(data_folder, 'schedule.json'), encoding="utf-8"
        ) as data_file:
            data: json = json.loads(data_file.read())
            for data_object in data:
                id: int = data_object.get("id", None)
                name: str = data_object.get(
                    "name", None
                )
                slug: str = data_object.get(
                    "slug", None
                )

                try:
                    schedule, created = (
                        Schedule.objects.get_or_create(
                            id=id,
                            name=name,
                            slug=slug,
                        )
                    )
                    if created:
                        schedule.save()
                        display_format = (
                            "\n schedule, {}, has been saved."
                        )
                        print(display_format.format(schedule))
                except Exception as ex:
                    print(str(ex))
                    msg: str = (
                        "\n\nSomething went wrong saving this schedule:"
                        " {}\n{}".format(name, str(ex))
                    )
                    print(msg)

    def import_addresses_from_file(self) -> None:
        data_folder: str = os.path.join(BASE_DIR, "data")
        with open(
            os.path.join(data_folder, 'clean_address.json'), encoding="utf-8"
        ) as data_file:
            data: json = json.loads(data_file.read())
            for data_object in data:
                name: str = data_object.get(
                    "address", None
                )
                lat: float = data_object.get(
                    "lat", None
                )
                lon: float = data_object.get(
                    "lon", None
                )

                try:
                    address, created = (
                        Address.objects.get_or_create(
                            name=name,
                            lat=lat,
                            lon=lon
                        )
                    )
                    if created:
                        address.save()
                        display_format = (
                            "\n address, {}, has been saved."
                        )
                        print(display_format.format(address))
                except Exception as ex:
                    print(str(ex))
                    msg: str = (
                        "\n\nSomething went wrong saving this address:"
                        " {}\n{}".format(name, str(ex))
                    )
                    print(msg)

    def import_cafe_from_file(self) -> None:
        data_folder: str = os.path.join(BASE_DIR, "data")
        with open(
            os.path.join(data_folder, 'Coffee_guide.json'), encoding="utf-8"
        ) as data_file:
            data: json = json.loads(data_file.read())
            for data_object in data:
                name: str = data_object.get(
                    "name", None
                )
                description: str = data_object.get(
                    "description", None
                )
                address_name = data_object.get(
                    "address", None
                )
                schedules = data_object.get(
                    "schedules", None
                )
                alternative = data_object.get(
                    "alternatives", None
                )
                roaster = data_object.get(
                    "roasters", None
                )
                additionals = data_object.get(
                    "additionals", None
                )
                is_alternatives = data_object.get(
                    "is_alternatives", False
                )
                availables = data_object.get(
                    "availables", None
                )
                drinks = data_object.get(
                    "drinks", None
                )
                image = data_object.get(
                    "image", None
                )
                user = CustomUser.objects.get(id=1)

                try:
                    cafe, created = (
                        Cafe.objects.get_or_create(
                            name=name,
                            description=description,
                            address=Address.objects.get(name=address_name),
                            organization=user,
                            is_alternatives=is_alternatives,
                        )
                    )
                    if created:
                        if alternative:
                            cafe.alternatives.set(alternative)
                        if additionals:
                            cafe.additionals.set(additionals)
                        if image:
                            image_path = os.path.join(BASE_DIR, f"data/images/{image}")
                            with open(image_path, 'rb') as img_file:
                                # Создаем объект File
                                img = File(img_file, name=Path(image_path).name)
                                # Сохраняем изображение в модели Cafe
                                cafe.image.save(img.name, img, save=True)

                        cafe.roasters.set(roaster)
                        cafe.availables.set(availables)
                        for schedule in schedules:
                            id = schedule['id']
                            start = schedule['start']
                            end = schedule['end']
                            cafe.schedule_in_cafe.create(
                                cafe_id=cafe.id,
                                schedules_id=id,
                                start=start,
                                end=end
                            )

                        for drink in drinks:
                            id = drink['id']
                            cost = drink['cost']
                            cafe.drink_in_cafe.create(
                                cafe_id=cafe.id,
                                drink_id=id,
                                cost=cost
                            )

                        display_format = (
                            "\n cafe, {}, has been saved."
                        )
                        print(display_format.format(cafe))
                except Exception as ex:
                    print(
                        alternative,
                        roaster,
                        additionals,
                        schedules,
                        drinks
                    )
                    msg: str = (
                        "\n\nSomething went wrong saving this cafe:"
                        " {}\n{}".format(name, str(ex))
                    )
                    print(msg)

    def create_admin(self, *args, **kwargs) -> None:
        try:
            CustomUser.objects.create_superuser(
                username=ADMIN_USERNAME,
                password=ADMIN_PASSWORD,
                email=ADMIN_EMAIL
            )
            print("суперпользователь создан")
        except Exception:
            print("суперпользователь уже существует")

    def handle(self, *args, **options) -> None:
        """
        Call the function to import data
        """
        self.import_additinals_from_file()
        self.import_roasters_from_file()
        self.import_drinks_from_file()
        self.import_alternatives_from_file()
        self.import_availables_from_file()
        self.import_schedules_from_file()
        self.import_addresses_from_file()
        self.create_admin()
        self.import_cafe_from_file()
