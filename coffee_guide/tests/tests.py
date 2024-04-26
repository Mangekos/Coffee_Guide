import re

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from cafe.models import Address, Alternative, Cafe, Roaster, Drink, Schedule, Additionals, Available
from api.serializers.cafe import CafeGetSerializer
from users.models import CustomUser


class CafeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('cafes-list')
        cls.address = Address.objects.create(name='Test Address', lat=0, lon=0)
        cls.alternative1 = Alternative.objects.create(name='TestAlternative1', slug="a1")
        cls.alternative2 = Alternative.objects.create(name='AnotherAlternative', slug="a2")
        cls.roaster1 = Roaster.objects.create(name='Test Roaster 1', slug="roaster1")
        cls.roaster2 = Roaster.objects.create(name='Test Roaster 2', slug="roaster2")
        cls.drink1 = Drink.objects.create(name='Test Drink 1', slug="testdrink1")
        cls.drink2 = Drink.objects.create(name='Test Drink 2', slug="testdrink2")
        cls.schedule1 = Schedule.objects.create(name="пн-пт", slug="budni")
        cls.schedule2 = Schedule.objects.create(name="сб-вс", slug="vihi")
        cls.additionals1 = Additionals.objects.create(name='dopoption1', slug="dopoption1")
        cls.additionals2 = Additionals.objects.create(name='dopoption2', slug="dopoption2")
        cls.available1 = Available.objects.create(name="hav_option1", slug="hav_option1")
        cls.available2 = Available.objects.create(name="hav_option2", slug="hav_option2")

    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', email='testuser@m.ru', organization_inn="512345678912")
        self.client.force_authenticate(user=self.user)
        self.cafe_data = {
            "name": "Тестовое кафе",
            "description": "Описание моего кафе",
            "address": 1,
            "schedules": [
                {
                "id": 1,
                "start": "08:00:00",
                "end": "18:00:00"
                },
                {
                "id": 2,
                "start": "09:00:00",
                "end": "17:00:00"
                }
            ],
            "alternatives": [1, 2],
            "roasters": [1, 2],
            "drinks": [
                {
                "id": 1,
                "cost": 100
                },
                {
                "id": 2,
                "cost": 150
                }
            ],
            "additionals": [ 1, 2],
            "availables": [1, 2],
            "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAApgAAAKYB3X3/OAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANCSURBVEiJtZZPbBtFFMZ/M7ubXdtdb1xSFyeilBapySVU8h8OoFaooFSqiihIVIpQBKci6KEg9Q6H9kovIHoCIVQJJCKE1ENFjnAgcaSGC6rEnxBwA04Tx43t2FnvDAfjkNibxgHxnWb2e/u992bee7tCa00YFsffekFY+nUzFtjW0LrvjRXrCDIAaPLlW0nHL0SsZtVoaF98mLrx3pdhOqLtYPHChahZcYYO7KvPFxvRl5XPp1sN3adWiD1ZAqD6XYK1b/dvE5IWryTt2udLFedwc1+9kLp+vbbpoDh+6TklxBeAi9TL0taeWpdmZzQDry0AcO+jQ12RyohqqoYoo8RDwJrU+qXkjWtfi8Xxt58BdQuwQs9qC/afLwCw8tnQbqYAPsgxE1S6F3EAIXux2oQFKm0ihMsOF71dHYx+f3NND68ghCu1YIoePPQN1pGRABkJ6Bus96CutRZMydTl+TvuiRW1m3n0eDl0vRPcEysqdXn+jsQPsrHMquGeXEaY4Yk4wxWcY5V/9scqOMOVUFthatyTy8QyqwZ+kDURKoMWxNKr2EeqVKcTNOajqKoBgOE28U4tdQl5p5bwCw7BWquaZSzAPlwjlithJtp3pTImSqQRrb2Z8PHGigD4RZuNX6JYj6wj7O4TFLbCO/Mn/m8R+h6rYSUb3ekokRY6f/YukArN979jcW+V/S8g0eT/N3VN3kTqWbQ428m9/8k0P/1aIhF36PccEl6EhOcAUCrXKZXXWS3XKd2vc/TRBG9O5ELC17MmWubD2nKhUKZa26Ba2+D3P+4/MNCFwg59oWVeYhkzgN/JDR8deKBoD7Y+ljEjGZ0sosXVTvbc6RHirr2reNy1OXd6pJsQ+gqjk8VWFYmHrwBzW/n+uMPFiRwHB2I7ih8ciHFxIkd/3Omk5tCDV1t+2nNu5sxxpDFNx+huNhVT3/zMDz8usXC3ddaHBj1GHj/As08fwTS7Kt1HBTmyN29vdwAw+/wbwLVOJ3uAD1wi/dUH7Qei66PfyuRj4Ik9is+hglfbkbfR3cnZm7chlUWLdwmprtCohX4HUtlOcQjLYCu+fzGJH2QRKvP3UNz8bWk1qMxjGTOMThZ3kvgLI5AzFfo379UAAAAASUVORK5CYII="
        }
        self.response = self.client.post(self.url, self.cafe_data, format='json')

    def test_create_cafe_authenticated(self):
        self.cafe_data['name'] = 'Тестовое кафе 2'
        response = self.client.post(self.url, self.cafe_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cafe.objects.count(), 2)
        self.assertEqual(Cafe.objects.get(pk=2).name, 'Тестовое кафе 2')

    def test_get_cafes_list(self):
        response = self.client.get(reverse('cafes-list'))
        cafes = Cafe.objects.all()
        serializer_data = CafeGetSerializer(cafes, many=True).data
        for item in response.data['results']:
            item['image']= re.search(
            r"http://testserver(.*)",
            item['image']).group(1)
        self.assertEqual(list(response.data['results']), serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_cafe_detail(self):
        cafe = Cafe.objects.get(name='Тестовое кафе')
        response = self.client.get(reverse('cafes-detail', kwargs={'pk': cafe.id}))
        response.data['image']= re.search(
            r"http://testserver(.*)",
            response.data['image']).group(1)
        serializer_data = CafeGetSerializer(cafe).data
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_cafe(self):
        cafe = Cafe.objects.get(pk=1)
        updated_data = {
            "name": "Обновленное кафе",
            "schedules": [
                {
                "id": 1,
                "start": "09:00:00",
                "end": "17:00:00"
                }
            ],
            "alternatives": [1],
            "roasters": [2],
            "drinks": [
                {
                "id": 1,
                "cost": 150
                },
                {
                "id": 2,
                "cost": 300
                }
            ],
            "additionals": [2],
            "availables": [1]
        }
        response = self.client.patch(
            reverse('cafes-detail', kwargs={'pk': cafe.id}),
            updated_data,
            format='json'
        )
        updated_cafe = cafe = Cafe.objects.get(pk=1)
        serializer_data = CafeGetSerializer(updated_cafe).data
        response.data['image']= re.search(
            r"http://testserver(.*)",
            response.data['image']).group(1)
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Cafe.objects.get().name, 'Обновленное кафе')

    def test_delete_cafe(self):
        cafe = Cafe.objects.get(name='Тестовое кафе')
        response = self.client.delete(
            reverse('cafes-detail', kwargs={'pk': cafe.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cafe.objects.count(), 0)
