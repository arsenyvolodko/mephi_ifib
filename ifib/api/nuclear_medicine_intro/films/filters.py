from django_filters import rest_framework as filters


class FilmsFilterSet(filters.FilterSet):
    id = filters.AllValuesMultipleFilter(
        field_name="id",
    )

    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )
