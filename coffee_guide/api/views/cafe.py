from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.cache import cache_page

from api.filters import CafeFilter, RoasterFilter
from api.paginations import CafePagination
from api.serializers.cafe import (
    AlternativeSerializer,
    CafeCreateSerializer,
    CafeGetSerializer,
    DrinkSerializer,
    ScheduleSerializer,
    AdditionalSerializer,
    AddressSerializer,
    RoasterSerializer,
)
from cafe.models import (
    Alternative,
    Cafe,
    Address,
    Additionals,
    Roaster,
    Drink,
    Schedule,
)
from drf_spectacular.utils import (
    # OpenApiParameter,
    extend_schema,
    extend_schema_view,
)
from rest_framework import viewsets


@extend_schema(
    tags=["Кофейня"],
    methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список заведений",
    ),
    retrieve=extend_schema(
        summary="Детальная информация о заведении",
    ),
    create=extend_schema(
        summary="Создать заведение",
    ),
    update=extend_schema(
        summary="Обновить заведение",
    ),
    partial_update=extend_schema(
        summary="Частичное обновление заведения",
    ),
    destroy=extend_schema(
        summary="Удалить заведение",
    ),
)
class CafeViewSet(viewsets.ModelViewSet):
    """Вьюсет: Кофейня"""

    queryset = Cafe.objects.all()
    filter_backends = [
        SearchFilter, DjangoFilterBackend
    ]
    search_fields = ["name", "address"]
    filterset_class = CafeFilter
    pagination_class = CafePagination
    # /api/cafe/?ordering=district

    def get_queryset(self):
        return Cafe.objects.prefetch_related(
            "drink_in_cafe__drink",
            "schedule_in_cafe__schedules",
            "additionals",
            "alternatives",
            "roasters",
        ).all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return CafeGetSerializer
        return CafeCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(organization=self.request.user)

    # def dispatch(self, request, *args, **kwargs):
    #     res = super().dispatch(request, *args, **kwargs)
    #     from django.db import connection
    #     for q in connection.queries:
    #         print('>>>>', q['sql'])
    #     print(f'Количество запросов в БД: {len(connection.queries)}')
    #     return res


@extend_schema(
    tags=["Адрес"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список адресов",
    ),
    retrieve=extend_schema(
        summary="Детальная информация об адресе",
    ),
)
class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


@extend_schema(
    tags=["Альтернатива"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список альтернатив",
    ),
    retrieve=extend_schema(
        summary="Детальная информация об альтернативе",
    ),
)
class AlternativeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alternative.objects.all()
    serializer_class = AlternativeSerializer


@extend_schema(
    tags=["Теги"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список тегов",
    ),
    retrieve=extend_schema(
        summary="Детальная информация о тегах",
    ),
)
class AdditionalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Additionals.objects.all()
    serializer_class = AdditionalSerializer


@extend_schema(
    tags=["Обжарщик"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список обжарщиков",
    ),
    retrieve=extend_schema(
        summary="Детальная информация об обжарщике",
    ),
)
class RoasterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Roaster.objects.all()
    serializer_class = RoasterSerializer
    filter_backends = [
        SearchFilter, DjangoFilterBackend
    ]
    search_fields = ["name"]
    filterset_class = RoasterFilter


@extend_schema(
    tags=["Напитки"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список напитков",
    ),
    retrieve=extend_schema(
        summary="Детальная информация о напитке",
    ),
)
class DrinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


@extend_schema(
    tags=["Время работы"],
    methods=["GET"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список расписания работы",
    ),
    retrieve=extend_schema(
        summary="Детальная информация о расписании работы",
    ),
)
class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
