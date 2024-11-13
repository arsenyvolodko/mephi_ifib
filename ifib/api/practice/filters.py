from django_filters import rest_framework as filters

from ifib.enums import PracticeGroupEnum


class PracticeFilterSet(filters.FilterSet):
    id = filters.AllValuesMultipleFilter(
        field_name="id",
    )

    practice_group = filters.AllValuesMultipleFilter(
        field_name="practice_group",
        choices=PracticeGroupEnum.choices
    )
