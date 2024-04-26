import django_filters

from cafe.models import Cafe, Alternative, Roaster, Address, Additionals


class CafeFilter(django_filters.FilterSet):
    """
    /api/v1/cafes/?name=your_cafe_name
    /api/v1/cafes/?address=your_address_name

    /api/v1/cafes/?is_alternatives=true
    /api/v1/cafes/?availables=alternative&availables=lactose_free_milk&availables=submarine&availables=la_marzocco&availables=sweater
    """

    address = django_filters.CharFilter(
        field_name="address__name",
        lookup_expr="icontains",
    )
    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )
    is_alternatives = django_filters.BooleanFilter(
        field_name="is_alternatives",
    )
    availables = django_filters.CharFilter(
        field_name="availables__slug",
        lookup_expr="icontains",
    )

    class Meta:
        model = Cafe
        fields = [
            "address",
            "name",
            "is_alternatives",
            "availables",
        ]


class RoasterFilter(django_filters.FilterSet):
    """
    /api/v1/roasters/?name=your_roaster_name
    """
    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = Roaster
        fields = [
            "name",
        ]
